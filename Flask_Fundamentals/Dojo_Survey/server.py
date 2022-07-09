from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "banana"

@app.route('/', methods=['post'])
def dojo_form():
    return render_template("index.html")

@app.route('/survey/submit', methods=['post'])
def submit_dojo():
    session['survey'] = request.form
    return redirect("/survey/display")

@app.route("/survey/display")
def display_dojo():
    return render_template("display.html", survey=session['survey'])

if __name__ == "__main__":
    app.run(debug=True)