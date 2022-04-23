#!/usr/bin/env python3

import requests

"""A script to interact with the Pokemon API, https://pokeapi.co/api/v2/pokemon?limit=100000&offset=0"""

API = "https://pokeapi.co/api/v2/pokemon"

def main():
	pokemon = requests.get(f"{API}?limit=100000&offset=0")
	get_pokemon = pokemon.json()
	count = get_pokemon['count']
	print(f"Total pokemon count: {count}")
	print(len(get_pokemon['results']))
	poke_list = get_pokemon['results']

	for monster in range(len(poke_list)):
		print(f"Pokemon: {poke_list[monster]['name']} found!!" )
		
	
	
	

if __name__ == "__main__":
	main()
