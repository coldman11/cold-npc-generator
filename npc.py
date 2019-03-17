import random


names_file = open('./assets/names.txt')
names_list = names_file.readlines()

surnames_file = open('./assets/surnames.txt')
surnames_list = surnames_file.readlines()
start_year = 1000


class Npc:
    def __init__(self, name, surname, birth_year, gender):
        self.name = name
        self.surname = surname
        self.birth_year = birth_year
        self.gender = gender

    def __str__(self):
        return 'Name: ' + self.name + 'Surname: ' + self.surname + \
               'Age: ' + str(self.get_age()) + '\nGender: ' + str(self.gender)

    def get_age(self):
        return start_year - self.birth_year


npcs = []


def generate_npcs(number):
    for number in range(number):
        npc = generate_npc()
        npcs.append(npc)


def generate_npc():
    name = names_list[random.randint(0, len(names_list))]
    surname = surnames_list[random.randint(0, len(surnames_list))]
    birth_year = random.randint(start_year - 100, start_year)
    gender = get_random_gender()
    npc = Npc(name, surname, birth_year, gender)
    return npc


def get_random_gender():
    return random.randint(0, 1)


generate_npcs(1)
print(npcs[0])



