print("running __init__ file")

from flask import Flask
app = Flask(__name__)
app.secret_key = "Silicon Valley Dojo = Best Dojo"