from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World!"

@app.route("/dojo")
def dojo():
    return "Dojo!"

@app.route("/say/<name>")
def say(name):
    return f"Hi {name}!"

@app.route("/repeat/<int:repeats>/<phrase>")
def repeat_phrase(repeats, phrase):
    return (phrase + " ") * repeats

if __name__ == "__main__":
    app.run(debug=True)

# Work in progress items
# NINJA BONUS: Ensure the names provided in the 3rd task are strings

# NINJA BONUS: For the 4th task, ensure the 2nd element in the URL is an integer, and the 3rd element is a string

# SENSEI BONUS: Ensure that if the user types in any route other than the ones specified, they receive an error message saying "Sorry! No response. Try again."