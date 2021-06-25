from app import app, db

class DbMixin(object):
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

class User(DbMixin, db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    telegram_id = db.Column(db.Integer, unique=True, nullable=False)

    def __init__(self, telegram_id):
        self.telegram_id = telegram_id
    