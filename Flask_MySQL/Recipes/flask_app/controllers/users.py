print("running users controller file")

from flask_app import app
from flask import render_template, redirect, session, request, flash
from flask_app.models.user import User
from flask_app.models.recipe import Recipe
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def login_reg_page():
    if "user_id" in session:
        del session["user_id"]
    return render_template("login_reg.html")

@app.route('/users/register', methods=['POST'])
def register_user():
    if not User.validate_user(request.form):
        print("Not Valid")
        return redirect('/')
    
    data = {
        "email": request.form['email']
    }
    user_in_db = User.get_one_by_email(data)

    if user_in_db:
        flash("Email already in use", "register")
        return redirect('/')
    else:
        print("It's Certainly Valid.")
        pw_hash = bcrypt.generate_password_hash(request.form["password"])
        print(pw_hash)

        data = {
            "first_name": request.form["first_name"],
            "last_name": request.form["last_name"],
            "email": request.form["email"],
            "password": pw_hash
        }

        # Register User
        user_id = User.save(data)
        print(f"New user has id: {user_id}")

        session["user_id"] = user_id
    return redirect('/main')

@app.route('/users/login', methods=['POST'])
def login_user():
    print(request.form['email'])
    data = {
        "email": request.form['email']
    }
    user_in_db = User.get_one_by_email(data)
    print(user_in_db)

    if not user_in_db:
        flash("Incorrect email and/or password.", "login")
        return redirect('/')
    
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash("Incorrect email and/or password.", "login")
        return redirect('/')
    
    session["user_id"] = user_in_db.id
    return redirect('/main')

@app.route('/main')
def main_page():
    if "user_id" not in session:
        return redirect('/')
    
    data = {
        "id": session['user_id']
    }
    user_in_db = User.get_one_by_id(data)

    all_recipies = Recipe.get_all()
    # print(all_recipies)
    # for recipie in all_recipies:
    #     print(recipie.name)
    #     print(recipie.under_30)
    #     print(recipie.user_id)

    return render_template("main.html", user_in_db=user_in_db, all_recipies=all_recipies)