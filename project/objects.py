from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User, PasswordGenerator, ObjectStorage
from . import db
import uuid
from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User, PasswordGenerator
from . import db

objects = Blueprint('objects', __name__)


@objects.route('/create_object')
@login_required
def create_object():
    return render_template('objects.html')


@objects.route('/save_object', methods=['POST'])
@login_required
def save_object():
    object = request.form.get('object')
    user_id = request.form.get('user_id')
    # object_uuid = str(uuid.uuid4())
    object_uuid = 'asddsas'
    new_object = ObjectStorage(user_id=user_id, object=object, uuid=object_uuid)
    # add the new user to the database
    db.session.add(new_object)
    db.session.commit()
    return 'saved'

