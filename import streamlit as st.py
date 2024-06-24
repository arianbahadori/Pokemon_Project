import streamlit as st
import requests
import json

st.title('Pokemon Explorer!')

# Element to pick the Pokémon number using number input
pokemon_number = st.number_input('Enter a number', 1, 898)

# Function to get the latest data on that Pokémon
def get_pokemon_data(pokemon_number):
    pokemon_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_number}"
    response = requests.get(pokemon_url)
    if response.status_code == 200:
        return response.json()
    else:
        st.error("Failed to retrieve Pokémon data.")
        return None

# Fetching the Pokémon data
pokemon_data = get_pokemon_data(pokemon_number)

if pokemon_data:
    # Display the full JSON response
    st.json(pokemon_data)
