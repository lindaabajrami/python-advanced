class Dog:
    def __init__(self,name):
        self.name = name

    def sound(self):
        print(f"{self.name} makes this sound: woof")

class Cat:
    def __init__(self,name):
        self.name = name

    def sound(self):
        print(f"{self.name} makes this sound: Meow")

class Bird:
    def __init__(self,name):
        self.name = name

    def sound(self):
        print(f"{self.name} makes this sound: Chirp")


dog = Dog("buddy")
cat = Cat("ruby")
bird = Bird("rose")

for animal in (dog,cat,bird):
    animal.sound()