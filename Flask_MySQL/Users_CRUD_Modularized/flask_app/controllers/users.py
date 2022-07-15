from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.models.user import User

@app.route('/')
def landing_page():
    return redirect("/users")

@app.route('/users')
def all_users():
    return render_template('read.html', users=User.get_all())

@app.route('/users/new')
def new_user_page():
    return render_template("create.html")

@app.route('/users/create', methods=['post'])
def create_user():
    User.save(request.form)
    return redirect("/users")