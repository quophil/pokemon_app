from flask import Flask, render_template, request
import requests

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def index():
    return render_template('layout.html')

@app.route('/', methods=['POST'])
def pokemon_search_result():
    pokemon_name_bleh = request.form['pokemon_name']
    return render_template('pk_bruv.html', pokemon_name = pokemon_name_bleh)
