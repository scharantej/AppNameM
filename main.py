
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("landing.html")

@app.route("/module1")
def module1():
    return render_template("module1.html")

@app.route("/module2")
def module2():
    return render_template("module2.html")

@app.route("/module3")
def module3():
    return render_template("module3.html")

if __name__ == "__main__":
    app.run(debug=True)
