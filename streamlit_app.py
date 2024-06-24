#Import the important libraries
import streamlit as st
import pandas as pd
import requests

#Title, function creation, user inputs
st.title("📊 Pokemon Facts Club")

def pokemon_data(pokemon_number):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_number}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()

first_pokemon = st.number_input(
    'type pokemon number between 1 and 155, then press enter', 1, 155,
    key='pokemon1')
second_pokemon = st.number_input(
    'type pokemon number between 1 and 155, then press enter', 1, 155,
    key='pokemon2')

pokemon_data1 = pokemon_data(first_pokemon)
pokemon_data2 = pokemon_data(second_pokemon)

if pokemon_data1 and pokemon_data2:
    pokemon_name1 = pokemon_data1["name"].title()
    pokemon_height1 = pokemon_data1['height']
    pokemon_weight1 = pokemon_data1['weight']
    pokemon_image1 = pokemon_data1['sprites']['front_default']
    
    pokemon_name2 = pokemon_data2["name"].title()
    pokemon_height2 = pokemon_data2['height']
    pokemon_weight2 = pokemon_data2['weight']
    pokemon_image2 = pokemon_data2['sprites']['front_default']

    col1, col2 = st.columns(2)

    with col1:
        st.image(pokemon_image1)
        st.title(pokemon_name1)
        st.write(pokemon_height1)
        st.write(pokemon_weight1)
        first_pokemon_card = pd.DataFrame({
            'Name': [pokemon_name1],
            "Height": [pokemon_height1],
            "Weight": [pokemon_weight1],
        })
        st.table(first_pokemon_card)
        
    with col2:
        st.image(pokemon_image2)
        st.title(pokemon_name2)
        st.write(pokemon_height2)
        st.write(pokemon_weight2)
        second_pokemon_card = pd.DataFrame({
            'Name': [pokemon_name2],
            "Height": [pokemon_height2],
            "Weight": [pokemon_weight2],
        })
        st.table(second_pokemon_card)

random_data = {
    "Questions": [
        "most beautiful pokemon?",
        "most popular pokemon?",
        "most hated pokemon?",
        "most funny pokemon?"
    ],
    "Answers": [
        "Milotic",
        "Pikachu",
        "Meowth",
        "Snorlax"
    ],
}
df = pd.DataFrame(random_data)
st.write(df)

st.write(
    ":balloon::balloon::Please do not feed the pokemons :balloon::balloon::balloon:"
)