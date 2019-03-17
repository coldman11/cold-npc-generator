class Npc:
    def __init__(self, name, surname, birth_year, gender):
        self.name = name
        self.surname = surname
        self.birth_year = birth_year
        self.gender = gender

    def __str__(self):
        return 'Name: ' + self.name + 'Surname: ' + self.surname + \
               'Born: ' + str(self.birth_year) + '\nGender: ' + str(self.gender)

