#!/usr/bin/env python3
import requests
import json
import time

API_BASE = "https://pokeapi.co/api/v2/"

def fetch(url):
    try:
        r = requests.get(url, timeout=10)
        r.raise_for_status()
        return r.json()
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None

def get_pokemon_by_type(p_type):
    data = fetch(API_BASE + f"type/{p_type}")
    if not data:
        return []
    return [p['pokemon']['name'] for p in data['pokemon']]

def get_pokemon_data(name):
    return fetch(API_BASE + f"pokemon/{name}")

def get_species(name):
    return fetch(API_BASE + f"pokemon-species/{name}")

def main():
    print("Template script to query PokeAPI. Fill logic per assignment.")

if __name__ == "__main__":
    main()
