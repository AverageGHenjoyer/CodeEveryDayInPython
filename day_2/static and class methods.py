class Person:
    population = 50

    def __init__(self, name, age):
        self.name = name,
        self.age = age

    def get_population(self, cls):
        return cls.population

    def is_adult(self, age):
        return age >= 18

    def display_info(self):
        print(f"{self.name} is {self.age} years old.")


newPerson = Person("Peter", 19)
newPerson.display_info()