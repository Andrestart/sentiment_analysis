from os import name
from flask import Flask, request, jsonify
import markdown.extensions.fenced_code
import tools.sql_tools_insert_api as sql
from textblob import TextBlob


app = Flask(__name__)

@app.route("/")
def index():
    readme_file = open("README.md", "r")
    md_template = markdown.markdown(readme_file.read(), extensions = ["fenced_code"])
    return md_template

@app.route("/characters")
def characters():
    everyone = sql.characters()
    return everyone

@app.route("/dialogue/<name>")
def todas(name):
    person = name
    frases = sql.todas_frases(person)
    return frases

@app.route("/newdialogue", methods=["POST"])
def insertamensaje():
        dialogue = request.form.get("dialogue")
        char_ = request.form.get("char")
        episode = request.form.get("episode")

        return sql.newdialogue(dialogue, char_,episode)
    
@app.route("/sent/<name>")
def ie(name):
    person = name
    dialogues = sql.toblob(person)
    blob = TextBlob(dialogues)
    return str(blob.sentiment)



app.run(debug=True)