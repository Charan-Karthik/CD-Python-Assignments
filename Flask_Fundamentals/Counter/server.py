from flask import Flask, render_template, redirect, session
app = Flask(__name__)
app.secret_key = "javascript"

@app.route('/')
def display_counter():
    if 'count' not in session:
        session['count'] = 1
    else:
        session['count'] += 1
    return render_template("index.html")

@app.route("/addtwo", methods=['post'])
def addtwo():
    session['count'] += 1 # since the redirect adds one, even though this is addtwo it should still increment by 1
    return redirect('/')

@app.route("/destroy_session", methods=['post'])
def clear_sesh():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True, port=5000)