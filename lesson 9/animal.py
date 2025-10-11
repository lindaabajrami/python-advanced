class Animal:
    def sound(self):
        print("some genetic animal sound.")

class Dog(Animal):
    def sound(self):
        print("Woof, Woof!")

class Cat(Animal):
    def sound(self):
        print("Meow, Meow!")

animal = Animal()
animal.sound()

dog = Dog()
dog.sound()

cat = Cat()
cat.sound()