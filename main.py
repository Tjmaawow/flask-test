from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Привет с Render!"

@app.route("/api/hello")
def api():
    return {"message": "Пример API JSON"}
