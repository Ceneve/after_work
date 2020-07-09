import hashlib


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    def __hash__(self):
        result = 17
        result = 31 * result + int(hashlib.sha256(self.name.encode("utf-8")).hexdigest(), 16)
        result = 31 * result + self.age
        return result


person1 = Person("Alex", 20)
person2 = Person("Alex", 20)
print(person1 == person2)
s = {person1, person2}
print(s)

