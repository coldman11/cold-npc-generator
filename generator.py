import random
from npc import Npc


female_names_file = open('./assets/female_names.txt')
female_names_list = female_names_file.readlines()

male_names_file = open('./assets/male_names.txt')
male_names_list = male_names_file.readlines()

surnames_file = open('./assets/surnames.txt')
surnames_list = surnames_file.readlines()
start_year = 1000


npcs = []


def generate_npcs(number):
    for number in range(number):
        npc = generate_npc()
        npcs.append(npc)


def generate_npc():
    gender = get_random_gender()
    name = get_random_name(gender)
    surname = surnames_list[random.randint(0, len(surnames_list))]
    birth_year = random.randint(start_year - 100, start_year)
    npc = Npc(name, surname, birth_year, gender)
    return npc


def get_random_gender():
    return random.randint(0, 1)


def get_random_name(gender):
    if gender == 0:
        return male_names_list[random.randint(0, len(male_names_list))]
    elif gender == 1:
        return female_names_list[random.randint(0, len(female_names_list))]


generate_npcs(1)
print(npcs[0])



