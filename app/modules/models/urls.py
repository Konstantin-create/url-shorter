from app import db
from datetime import datetime


class Url(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String, unique=True)
    short_url = db.Column(db.String, unique=True)
    time_stamp = db.Column(db.DateTime, default=datetime.utcnow())

    def __repr__(self):
        return f'<Url: {self.short_url} | {self.url}>'


class EmptyUrl:
    id = -1
    url = ''
    short_url = ''
    timestamp = datetime.utcnow()

    def __repr__(self):
        return '<EmptyUrl: -1>'
