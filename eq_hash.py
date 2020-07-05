class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    def __hash__(self):
        return hash((self.name, self.age))


person1 = Person("Alex", 20)
person2 = Person("Alex", 20)
print(person1 == person2)

