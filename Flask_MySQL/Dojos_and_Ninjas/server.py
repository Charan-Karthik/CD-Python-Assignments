print("running server filer")

from flask_app import app
# import controllers (controller stores all routes)
from flask_app.controllers import dojos
from flask_app.controllers import ninjas

if __name__ == "__main__":
    app.run(debug = True) # can add ", port=5000" to this if it ever stops working