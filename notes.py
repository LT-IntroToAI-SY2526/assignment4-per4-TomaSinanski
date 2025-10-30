# object oriented programming

# (define-struct dog [fur_color name age favorite_food])
class Dog:
    def __init__(self, breed, fur_color, name, age):
        self.breed = breed
        self.fur_color = fur_color
        self.name = name
        self.age = age

if __name__ == "__main__":
    berg_dog = Dog("labrador", "black", "Logan", 9)