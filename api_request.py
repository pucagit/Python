import requests

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon(pokemon_name):
    url = base_url + "pokemon/" + pokemon_name
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {
            "name": data["name"],
            "height": data["height"],
            "weight": data["weight"],
            "types": [type["type"]["name"] for type in data["types"]]
        }
    else:
        print("Error: ", response.status_code)

print(get_pokemon("pidgeotto"))