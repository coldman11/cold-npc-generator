import random
from npc import Npc
from attribute_generator import AttributeGenerator


start_year = 2019
attr = AttributeGenerator()

npcs = []


def generate_npcs(number):
    for number in range(number):
        npc = generate_npc()
        npcs.append(npc)


def generate_npc():
    gender = attr.random_gender()
    name = attr.random_name(gender)
    surname = attr.random_surname()
    birth_year = start_year
    max_age = random.randint(50, 120)
    npc = Npc(name, surname, birth_year, gender, max_age)
    return npc


generate_npcs(1)
print(npcs[0])
