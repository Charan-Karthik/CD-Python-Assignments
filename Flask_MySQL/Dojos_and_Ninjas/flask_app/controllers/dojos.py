print("running dojos controller file")

from flask_app import app
# ^ the app variable is what we're using to send/receive information for routes
from flask import render_template, redirect, session, request
# import model
from flask_app.models.dojo import Dojo # import class from model

@app.route('/')
def landing_page():
    all_dojos = Dojo.get_all()
    return render_template("dojos.html", all_dojos=all_dojos)

@app.route('/new/dojo', methods=['POST'])
def submit_new_dojo():
    Dojo.save(request.form)
    return redirect('/')

@app.route('/dojo/<int:id>')
def single_dojo_page(id):
    data = {
        "id": id
    }

    dojo = Dojo.ninjas_in_dojo(data)
    # print(dojo.name)
    return render_template("dojo_show.html", dojo = dojo)