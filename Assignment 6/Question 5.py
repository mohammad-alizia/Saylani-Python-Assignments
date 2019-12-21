class Car:

    def __init__(self, name, model, color):
        self.name = name
        self.model = model
        self.color = color

    def name(self):
        return (self.name)

    def model(self):
        return (self.model)

    def color(self):
        return (self.color)

obj1 = Car(
    "Vitz",
    2013,
    "black"
)

obj2 = Car(
    "Mehran",
    2019,
    "blue"
)
obj3 = Car(
    "Aqua",
    2018,
    "white"
)
print("==========\nFirst Car")
print(obj1.name)
print(obj1.color)
print(obj1.model)
print("==========")

print("\n==========\nSecond Car")
print(obj2.color)
print(obj2.model)
print(obj2.name)
print("==========")

print("\n==========\nThird Car")
print(obj3.name)
print(obj3.color)
print(obj3.model)
print("==========")