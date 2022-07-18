from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.models.user import User

@app.route('/')
def landing_page():
    return redirect("/users")

@app.route('/users')
def all_users():
    return render_template('read.html', users=User.get_all())

@app.route('/user/new')
def new_user_page():
    return render_template("create.html")

@app.route('/users/create', methods=['post'])
def create_user():
    User.save(request.form)
    return redirect("/users")

@app.route('/user/update/<int:id>')
def update_user(id):
    data = {
        "id":id
    }
    user = User.get_user(data)
    return render_template("update.html", user=user)

@app.route('/user/update',methods=['POST'])
def update():
    User.update(request.form)
    return redirect('/users')

@app.route('/user/<int:id>')
def single_user(id):
    data = {
        "id":id
    }
    user = User.get_user(data)
    return render_template("single_user.html", user=user)

@app.route('/delete/<int:id>')
def delete_user(id):
    data = {
        "id":id
    }
    User.delete_user(data)

    return redirect('/users')