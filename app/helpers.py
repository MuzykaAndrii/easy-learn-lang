from functools import wraps
from app.models import User
from app import cache

# @cache.memoize(600)
def get_user(user_telegram_id):
    print('Executed query to database')
    return User.query.filter_by(telegram_id=user_telegram_id).first()

def manage_user(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        response = args[0]
        current_user_telegram_id = response.chat.id
        current_user = get_user(current_user_telegram_id)

        if not current_user:
            new_user = User(current_user_telegram_id)
            try:
                new_user.save()
            except BaseException:
                print(f'Failed to save user to database, telegram_id: {current_user_telegram_id}')
                bot.send_message(current_user_telegram_id, "Database error, please repeat it one more time.")

        return f(*args, **kwargs)
    return decorated_function