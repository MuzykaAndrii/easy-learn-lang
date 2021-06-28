from functools import wraps
from app.models import User
from app import cache

def manage_user(f):
    @wraps(f)
    # @cache.cached(timeout=86400)
    def decorated_function(*args, **kwargs):
        print(dir(args))
        # response = kwargs['message']
        # current_user_telegram_id = response.chat.id
        # current_user = User.query.filter_by(telegram_id=current_user_telegram_id).first()

        # if not current_user:
        #     new_user = User(current_user_telegram_id)
        #     try:
        #         new_user.save()
        #     except BaseException:
        #         print(f'Failed to save user to database, telegram_id: {current_user_telegram_id}')
        #         bot.send_message(current_user_telegram_id, "Database error, please repeat it one more time.")

        return f(*args, **kwargs)
    return decorated_function