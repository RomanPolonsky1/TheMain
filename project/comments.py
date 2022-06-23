from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User, PasswordGenerator, ObjectComment
from . import db

comments_bp = Blueprint('comments', __name__)

@comments_bp.route('/create_comment')
@login_required
def comments():
    return render_template('comments.html')


@comments_bp.route('/save_comment', methods=['POST'])
@login_required
def save_comment():
    new_comment = request.form.get('comment')
    if len(new_comment) > 0:
        me = ObjectComment(user_id=current_user.id, data=new_comment)
        db.session.add(me)
        db.session.commit()
    return render_template("comment_saved.html", username=current_user.name)
    # return 'comment saved'
