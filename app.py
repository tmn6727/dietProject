from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "jetsjets"

@app.route("/diet")
def index():
	flash("What's your name")
	return render_template("index.html")

@app.route("/greet", methods=["Post", "Get"])
def greet():
	flash("Hi " + str(request.form['name_input']) + ", great to see you")
	return render_template("index.html")
