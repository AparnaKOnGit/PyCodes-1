# Sample Class Person
class Person:
    def __init__(self, name):
        self.name = name

    def sayHiToPerson(self):
        print("Hii ", self.name)


def class_example() -> Person:
    p1: Person = Person("Sruthi")
    p1.sayHiToPerson()
    return p1


def list_demo():
    lp: list = [class_example().name, "Pranav", "Mahesh", "Aparna"]
    print(lp[:3])
    print(lp[1:])
    print(lp[-2:])

