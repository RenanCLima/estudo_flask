from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb+srv://renancesarlima:hLXU67Hden3JmEVn@dbflask.pi5q12a.mongodb.net/")
db = client["db_estudo_flask"]
collection = db["minhaColecao"]

@app.route('/')
def index():
    items = collection.find()
    return render_template("index.html", items=items)

if __name__ == "__main__":
    app.run(debug=True)