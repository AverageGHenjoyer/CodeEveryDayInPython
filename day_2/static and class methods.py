class Person(object):
    population = 50

    def __init__(self, name, age):
        self.name = name,
        self.age = age

    @classmethod
    def get_population(cls):
        return cls.population

    @staticmethod
    def is_adult(age):
        return age >= 18

    def display_info(self):
        print(f"{self.name} is {self.age} years old.")


newPerson = Person("Peter", 19)
newPerson.display_info()
print(Person.is_adult(17))
print(Person.get_population())