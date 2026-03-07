import json
from functools import reduce

f = open("/home/gabriel/Documentos/Projeto/banco/Encoder/projetos/aquario/aquarium.json" , encoding="utf8")
data_aquarium = json.load(f)

animals = data_aquarium["data"]

def pick_animal_type(animal):
    return animal["type"], 1

def reducer(acc , val):

    if val[0] not in acc.keys():
        acc[val[0]] = 0 + val[1]
    else:
        acc[val[0]] = acc[val[0]] + val[1]

    return acc

type_animals = list(map(pick_animal_type, animals))

print(type_animals)

type_animals_count = reduce(reducer, type_animals, {})
print(type_animals_count)

