print("running ninjas controller file")

from flask_app import app
# ^ the app variable is what we're using to send/receive information for routes
from flask import render_template, redirect, session, request
# import model
from flask_app.models.ninja import Ninja # import class from model
from flask_app.models.dojo import Dojo

@app.route('/new/ninja')
def new_ninja_page():
    all_dojos = Dojo.get_all()
    return render_template("new_ninja.html", all_dojos=all_dojos)

@app.route('/new/ninja/submit', methods=['POST'])
def submit_new_ninja():
    Ninja.save(request.form)
    return redirect('/')