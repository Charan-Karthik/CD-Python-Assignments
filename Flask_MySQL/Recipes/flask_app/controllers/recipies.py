from flask_app import app
from flask import render_template, redirect, session, request, flash
from flask_app.models.recipe import Recipe
from flask_app.models.user import User

@app.route('/recipies/create')
def create_recipe():
    return render_template("new_recipe.html")

@app.route('/recipies/submit', methods=['POST'])
def submit_new_recipe():
    if "user_id" not in session:
        return redirect('/')
    
    data = {
        "name": request.form["name"],
        "description": request.form["description"],
        "instructions": request.form["instructions"],
        "date_made": request.form["date_made"],
        "under_30": request.form["under_30"],
        "user_id": session["user_id"]
    }

    Recipe.save(data)
    return redirect('/main')

@app.route('/show/recipe/<int:id>')
def show_recipe(id):
    data = {
        "id": session['user_id']
    }
    user_in_db = User.get_one_by_id(data)

    one_recipe = Recipe.get_one_recipe({"id":id})
    all_recipies = Recipe.get_all()

    user_data = {
        "id": one_recipe.user_id
    }
    user = User.get_one_by_id(user_data)
    
    return render_template("show_recipe.html", user_in_db=user_in_db, one_recipe=one_recipe, all_recipies=all_recipies, user=user)

@app.route('/edit/recipe/<int:id>')
def edit_recipe(id):
    one_recipe = Recipe.get_one_recipe({"id":id})

    return render_template("edit_recipe.html", one_recipe=one_recipe)

@app.route('/update/recipe/<int:id>', methods=['POST'])
def update_recipe(id):
    print(f"Trying to edit recipe {id}")
    
    data = {
        "name": request.form["name"],
        "description": request.form["description"],
        "instructions": request.form["instructions"],
        "date_made": request.form["date_made"],
        "under_30": request.form["under_30"],
        "id": id
    }
    Recipe.edit_recipe(data)

    return redirect('/main')

@app.route('/delete/<int:id>')
def delete_recipe(id):
    print(f"Trying to delete recipe {id}")

    data = {
        "id":id
    }
    Recipe.delete_recipe(data)

    return redirect("/main")