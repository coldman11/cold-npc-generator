import random


names_file = open('./assets/names.txt')
names_list = names_file.readlines()

surnames_file = open('./assets/surnames.txt')
surnames_list = surnames_file.readlines()
start_year = 1000


class Npc:
    def __init__(self, name, surname, birth_year):
        self.name = name
        self.surname = surname
        self.birth_year = birth_year

    def __str__(self):
        return 'Name: ' + self.name + \
               'Surname: ' + self.surname + \
               'Age: ' + str(self.get_age())

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
    npc = Npc(name, surname, birth_year)
    return npc


generate_npcs(1)
print(npcs[0])



