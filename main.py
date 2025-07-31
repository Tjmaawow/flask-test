from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/login")
def login():
    return

@app.route("/register")
def register():
    return

app.run(debug=True)