from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/loginFallback", methods=["POST"])
def loginFallback():
    email = request.form.get("email")
    passw = request.form.get("password")
    return {"email":email, "password":passw}

@app.route("/register")
def register():
    return render_template("register.html")

app.run(debug=True)