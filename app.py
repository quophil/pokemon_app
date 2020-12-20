from flask import Flask, render_template, request
import requests

app = Flask(__name__)
app.config['DEBUG'] = True

url = "https://pokeapi.co/api/v2/pokemon/{}"

@app.route('/')
def index():
    return render_template('layout.html')

@app.route('/', methods=['POST'])
def pokemon_search_result():
    pokemon_entry = request.form['pokemon_entry']
    r = requests.get(url.format(pokemon_entry.lower())).json()
    pokemon = {
        'pokemon_name': r['species']['name'],
        'pokemon_index': r['game_indices']['19']['game_index'],
        'pokemon_type1': r['types']['0']['type']['name'],
        'pokemon_type2': 'No Type 2',
        'pokemon_weight': r['types']['weight'],
        'pokemon_height': r['game_indices']['height']
    }

    if len(r['types']) >= 3:
        pokemon['pokemon_type2'] = r['types']['1']['type']['name']
    return render_template('pokemon_template.html', 
    pokemon_name=pokemon['pokemon_name'], 
    pokemon_index=pokemon['pokemon_index'],
    pokemon_type1=pokemon['pokemon_type1'],
    pokemon_type2=pokemon['pokemon_type2'],
    pokemon_weight=pokemon['pokemon_weight'],
    pokemon_height=pokemon['pokemon_height']
    )