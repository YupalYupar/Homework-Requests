from pprint import pprint

import requests

def inteligens_Hulk():
    url = "https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/powerstats/332.json"
    response = requests.get(url)
    pok = response.json()
    print(f"интелект Hulk - {pok['intelligence']}")

if __name__ == "__main__":
    inteligens_Hulk()

def inteligens_Capt_America():
    url = "https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/powerstats/149.json"
    response = requests.get(url)
    pok = response.json()
    print(f"интелект Captain America - {pok['intelligence']}")

if __name__ == "__main__":
    inteligens_Capt_America()

def inteligens_Thanos():
    url = "https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/powerstats/655.json"
    response = requests.get(url)
    pok = response.json()
    print(f"интелект Thanos - {pok['intelligence']}")

if __name__ == "__main__":
    inteligens_Thanos()
