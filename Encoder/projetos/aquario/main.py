import json

f = open("Encoder/projetos/aquario/aquarium.json", encoding="utf8")
data_aquarium = json.load(f)
animals = data_aquarium["data"]

def verify_saltwater(animal):
    if animal["type"] == "saltwater":
        return True
    return False

animals_saltwater = list(filter(verify_saltwater, animals))

def animal_name(animal):
    return animal["name"]

animals_saltwater_name = list(map(animal_name, animals_saltwater))
print(animals_saltwater_name)

def assign_to_tank(animals, names_selected, new_tank_number):
    def change_tank_number(animal):
        if animal["name"] in names_selected:
            animal["tank-number"] = new_tank_number
        return animal
    return list(map(change_tank_number, animals))

new_aquarium = assign_to_tank(animals, animals_saltwater_name, 42)
print(new_aquarium)
