from z_folder.dictionary_healthy150 import add_item


class Person:
    def __init__(self, person_id, name, age, gender):
        self.person_id = person_id
        self.name = name
        self.age = age
        self.gender = gender

    def add_personal_data(self):
	    add_item(self.person_id, 'personal data', name = self.name, age = self.age, gender = self.gender)