import random


class AttributeGenerator:
    def __init__(self):
        self.female_names = open('./assets/female_names.txt').readlines()
        self.male_names = open('./assets/male_names.txt').readlines()
        self.surnames = open('./assets/surnames.txt').readlines()

    def random_gender(self):
        return random.randint(0, 1)

    def random_name(self, gender):
        if gender == 0:
            return self.male_names[random.randint(0, len(self.male_names))]
        elif gender == 1:
            return self.female_names[random.randint(0, len(self.female_names))]
        else:
            return 'Unknown'

    def random_surname(self):
        return self.surnames[random.randint(0, len(self.surnames))]

