class Animal:
    def __init__(self,name):
        self.name = name

    def sound(self):
        print("some genetic animal sound")

    def description(self):
        print(f"this is named {self.name}")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def sound(self):
        print("woof, woof!")

    def description(self):
        super().description()
        print(f"breed: {self.breed}")

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def sound(self):
        print("Meow, Meow")

    def description(self):
        super().description()
        print(f"color: {self.color}")

animal = Animal("Generic Animal")
animal.sound()
animal.description()

dog =Dog( "rex", "Golden Retriever")
dog.sound()
dog.description()

cat = Cat( "Whiskers", "black")
cat.sound()
cat.description()
