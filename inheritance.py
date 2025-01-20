# Base class (superclass)
class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        pass

# Subclass
class Dog(Animal):
    def make_sound(self):
        return "Woof!"

# Subclass
class Cat(Animal):
    def make_sound(self):
        return "Meow!"

# Create instances
dog_instance = Dog(name="Buddy")
cat_instance = Cat(name="Whiskers")

# Access attributes and call methods
print(dog_instance.name)     # Output: Buddy
print(dog_instance.make_sound())  # Output: Woof!

print(cat_instance.name)     # Output: Whiskers
print(cat_instance.make_sound())  # Output: Meow!
