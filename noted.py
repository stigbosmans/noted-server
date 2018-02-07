from flask import Flask, jsonify, request
from notebook import Notebook
import os
app = Flask(__name__)

if not os.path.exists("notebooks"):
    os.makedirs("notebooks")

@app.route("/")
def get():
    return jsonify({"jan": "OK"})

@app.route("/", methods=["POST"])
def post():
    req = request.get_json()
    notebook_name = req["notebook"]
    content = req["content"]
    page_name = req["pageName"]
    notebook = Notebook(notebook_name)
    notebook.add_page(page_name, content)
    return '', 200

if __name__ == '__main__':
     app.run(port=5002)