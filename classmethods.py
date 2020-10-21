from datetime import date


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

        # a class method to create a

    # Person object by birth year.
    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name, date.today().year - year)


person1 = Person('mayank', 21)
person2 = Person.fromBirthYear('mayank', 1996)

print(person1.age)
print(person2.age)
