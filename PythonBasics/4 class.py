# Exercise 1 ----------------------------
# Inheritance/object
# Classes can have functions and data associated with the class
class Dog:
    name = 'Jon'
    color = 'brown'

# Object oriented programming/instance
instance = Dog()
obj = Dog()
object = Dog()

instance.name
obj.name 

# Exercise 2 ----------------------------
class Dog:
    name = 'Jon'
    color = 'brown'
    def get_color(self):
        return self.color

obj = Dog()
obj.get_color()

# Exercise 3 ----------------------------
class Animal():
    noise = "Grunt"
    size = "Large"
    color = "brown"
    hair = "covers body"
    def get_color(self):
        return self.color
    def make_noise(self):
        return self.noise
    
dog = Animal()
dog.make_noise()
dog.size = "small"
dog.color = "black"
dog.hair = "hairless"

class Dog(Animal): 
    name = 'Jon'
    size = 'small'
    color = 'black'
    age = 19
    
jon = Dog()
jon.color = 'white'
jon.name = 'Jon Snow'

dog.hair
new_dog = Dog() # dog class v.s. animal class
new_dog.name # animal class has the name of Jon
# inheriting from animal 
new_dog.size
new_dog.color
new_dog.age

# Exercise 4 ----------------------------
# self is referring to an instance you create
class Animal():
    noise = "Grunt"
    size = "Large"
    color = "brown"
    hair = "covers body"
    def get_color(self, abc):
        return self.color + " " + abc
    @property
    def make_noise(self):
        return self.noise

dog = Animal()
dog.get_colour("red")
dog.make_noise