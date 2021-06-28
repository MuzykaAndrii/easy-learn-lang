from app import app, db
import json

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
    bundles = db.relationship('Bundle', backref='creator', lazy='dynamic')

    def __init__(self, telegram_id):
        self.telegram_id = telegram_id

class Bundle(DbMixin, db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    creator_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    words = db.Column(db.Text)

    def __init__(self, creator_id):
        self.creator_id = creator_id
    
    def encode_words(self, dict_words):
        self.words = json.dumps(dict_words, ensure_ascii=False)
    
    def decode_words(self):
        return json.loads(self.words)