from flask import Blueprint, render_template, request, jsonify, url_for
from flask_login import login_required, current_user
from project.password_generator import password_as_uuid
from .models import User, PasswordGenerator, NoteStorage, ObjectStorage
from flask_login import login_user, logout_user, login_required
from . import db
import uuid
import json
import jsonpickle
from json import JSONEncoder

# export FLASK_APP=project
# export FLASK_DEBUG=1

main = Blueprint('main', __name__)


@main.route('/')
def index():
	return render_template('index.html')
	# return render_template('password_generator.html', password=password_as_uuid().hex)


@main.route('/profile')
@login_required
def profile():
	return render_template('profile.html', name=current_user.name)


@main.route('/passgen')
@login_required
def passgen():
	return render_template('password_generator.html', password=password_as_uuid().hex)


@main.route('/save_password', methods=['POST'])
@login_required
def save_password():
	password = request.form.get('password')
	text = request.form.get('text')
	me = PasswordGenerator(user_id=current_user.id, password=password, text=text)
	db.session.add(me)
	db.session.commit()
	# return render_template("password_saved.html", username=current_user.name)
	return jsonify(user_id=current_user.id, password=password, text=text)


@main.route('/save_note', methods=['POST'])
@login_required
def save_note():
	note = request.form.get('note')
	if len(note) > 0:
		me = NoteStorage(user_id=current_user.id, note=note)
		db.session.add(me)
		db.session.commit()
	return render_template("note_saved.html", username=current_user.name)


@main.route('/list_password')
@login_required
def list_password():
	passwords = PasswordGenerator.query.filter_by(user_id=current_user.id).all()
	return render_template('list_password.html', passwords=passwords)
	# print('---------------')
	# print(passwords[1].__dict__)
	# lists = []
	# for i in passwords:
	# 	dic = {}
	# 	dic['text'] = i.text
	# 	dic['password'] = i.password
	# 	lists.append(dic)
	# return render_template('list_password.html', passwords=passwords)
	# return 'okay'


@main.route('/list_passwords_json')
@login_required
def list_passwords_json():
	passwords = PasswordGenerator.query.filter_by(user_id=current_user.id).all()
	# return render_template('list_password.html', passwords=passwords)
	print('---------------')
	print(passwords[1].__dict__)
	lists = []
	for i in passwords:
		dic = {}
		dic['text'] = i.text
		dic['password'] = i.password
		lists.append(dic)
		# print("dic:")
		# print(dic)
		# lists.append(dic)
	# print("list:")
	# print(lists)
	return jsonify(lists)
	# return render_template('list_password.html', passwords=list)


@main.route('/create_note')
@login_required
def create_note():
	notes = NoteStorage.query.filter_by(user_id=current_user.id).all()
	return render_template('note.html', notes=notes)


@main.route('/create_object')
@login_required
def create_object():
	return render_template('objects.html')


@main.route('/save_object', methods=['POST'])
@login_required
def save_object():
	object = request.form.get('object')
	# user_id = request.form.get('user_id')
	object_uuid = uuid.uuid4()
	# object_uuid = 'asddsas'
	new_object = ObjectStorage(user_id=current_user.id, object=object, object_uuid=str(object_uuid))
	# add the new user to the database
	db.session.add(new_object)
	db.session.commit()
	return str(object_uuid)


@main.route('/object_list')
@login_required
def object_list():
	objects = ObjectStorage.query.filter_by(user_id=current_user.id).all()
	# print(current_user.id)
	# print(objects)
	lists = []
	for obj in objects:
		dic = {}
		dic['object_uuid'] = obj.object_uuid
		dic['object'] = obj.object
		lists.append(dic)
	return jsonify(lists)
