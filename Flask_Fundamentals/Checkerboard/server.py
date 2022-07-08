from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def normal_checkerboard():
    return render_template("index.html", row=8, col=8, color1="red", color2="black")

@app.route("/<int:row>")
def enter_row(row):
    return render_template("index.html", row=row, col=8, color1="red", color2="black")

@app.route("/<int:row>/<int:col>")
def row_and_col(row, col):
    return render_template("index.html", row=row, col=col, color1="red", color2="black")

@app.route("/<int:row>/<int:col>/<color1>/<color2>")
def define_colors_too(row, col, color1, color2):
    return render_template("index.html", row=row, col=col, color1=color1, color2=color2)

if __name__=="__main__":
    app.run(debug=True)