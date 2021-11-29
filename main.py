from os import name
from flask import Flask, request, jsonify
import markdown.extensions.fenced_code
import tools.sql_tools_insert_api as sql
from textblob import TextBlob


app = Flask(__name__)

@app.route("/")
def index():
    readme_file = open("infoapi.md", "r")
    md_template = markdown.markdown(readme_file.read(), extensions = ["fenced_code"])
    return md_template

@app.route("/characters")
def characters():
    everyone = sql.characters()
    return everyone

@app.route("/episodes")
def epi():
    allepisodes = sql.episodes()
    return allepisodes

@app.route("/dialogue/<name>")
def todas(name):
    person = name
    frases = sql.alldialogues(person)
    return frases

@app.route("/newdialogue", methods=["POST"])
def insertdialogue():
        dialogue = request.form.get("dialogue")
        char_ = request.form.get("char")
        episode = request.form.get("episode")

        return sql.newdialogue(dialogue, char_,episode)
    
@app.route("/dialogue/<name>/sent")
def blob(name):
    dialogues = sql.toblob(name)
    blob = TextBlob(dialogues)
    return str(blob.sentiment)

@app.route("/all/sent")
def allblob():
    dialogues = sql.alltoblob()
    blob = TextBlob(dialogues)
    return str(blob.sentiment)

@app.route("/dialogues")
def dia():
    all = sql.alltoblob()
    return all


app.run(debug=True)