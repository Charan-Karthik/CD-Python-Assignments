print("running init file")

from flask import Flask
app = Flask(__name__)
app.secret_key = "mom's recipe is the best recipe"