class Dog:
    # Class variable — shared by ALL dogs
    species = "Canis familiaris"
    total_dogs = 0

    def __init__(self, name, breed, age):
        self.name = name        # instance variable
        self.breed = breed      # instance variable
        self.age = age          # instance variable
        Dog.total_dogs += 1     # every time a dog is created, counter goes up

    def bark(self):
        print(f"{self.name} says: Woof!")

    def birthday(self):
        self.age += 1
        print(f"Happy Birthday {self.name}! You are now {self.age} years old")

    def info(self):
        print(f"{self.name} is a {self.breed}, {self.age} years old")


dog1 = Dog("Bruno", "Labrador", 3)
dog2 = Dog("Max", "Poodle", 5)
dog3 = Dog("Bella", "Husky", 2)

print(Dog.total_dogs)      # 3
print(dog1.species)        # Canis familiaris
print(dog2.species)        # Canis familiaris — same for all