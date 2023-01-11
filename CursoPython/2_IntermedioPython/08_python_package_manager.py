### Python Package Manager ###

#PIP https://pypi.org

#pip install pip
#pip --version

#pip install numpy
import numpy 
import pip
print(numpy.version.version)
print(pip.__version__)

numpy_array=numpy.array([35,24,62,52,30,30,17])
print(type(numpy_array))
print(numpy_array*2)

import pandas # pip install pandas

#pip list
#pip unistall pandas
#pip show numpy

#pip install requests
import requests

response =requests.get("https://pokeapi.co/api/v2/pokemon?limit=151")
print(response)
print(response.status_code)
#print(response.json())#Trae doscientos pokemon
#print(pokemondict["results"])Es lo mismo a lo de arriba
pokemondict = response.json()
print(pokemondict.keys())
print(pokemondict["count"])
print(pokemondict["next"])
print(pokemondict["previous"])

pokemon=[]
pokemonlist =pokemondict["results"]
print(type(pokemonlist))
print(type(pokemonlist[1]))
for i in range(len(pokemonlist)):
    pokemon.append(pokemonlist[i]["name"])
    print(pokemon[i])
#print(pokemon)
#print(len(pokemon))

# Arithmetics Package

from mypackage import arithmetics

print(arithmetics.sum_two_values(1,7))