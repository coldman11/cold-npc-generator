class Npc:
    def __init__(self, name, surname, birth_year, gender, max_age):
        self.name = name
        self.surname = surname
        self.birth_year = birth_year
        self.gender = gender
        self.alive = True
        self.max_age = max_age
        self.death_year = None

    def __str__(self):
        return 'Name: ' + self.name + 'Surname: ' + self.surname + \
               'Born: ' + str(self.birth_year) + \
               '\nDied: ' + str(self.death_year) + \
               '\nGender: ' + str(self.gender) + \
               '\nAlive: ' + str(self.alive) + \
               '\nMax age: ' + str(self.max_age)


    def kill(self):
        self.alive = False

    def get_age(self, year):
        return year - self.birth_year

    def set_death_year(self, year):
        self.death_year = year

