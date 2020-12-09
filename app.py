from flask import Flask, render_template, request
import requests

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def pokemon_search_result():
    pokemon_name = request.form['pokemon_name']
    return pokemon_name