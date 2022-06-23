from flask_login import UserMixin
from . import db


class User(UserMixin, db.Model):
	id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
	email = db.Column(db.String(100), unique=True)
	password = db.Column(db.String(100))
	name = db.Column(db.String(1000))


class PasswordGenerator(UserMixin, db.Model):
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer)
	password = db.Column(db.String(255))
	text = db.Column(db.String(255))


class NoteStorage(UserMixin, db.Model):
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer)
	note = db.Column(db.String(255))


class ObjectStorage(UserMixin, db.Model):
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer)
	object = db.Column(db.String(255))
	object_uuid = db.Column(db.String(255))
	# object_id = db.Column(db.String(255))
	# data3 = db.Column(db.String(255))
	# data1 = db.Column(db.String(255))


class ObjectComment(UserMixin, db.Model):
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer)
	comment = db.Column(db.String(255))
	object_uuid = db.Column(db.String(255))
