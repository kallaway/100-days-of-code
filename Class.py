class Dog:
    # This runs automatically when you create a Dog
    def __init__(self, name, breed, age):
        self.name = name      # instance variable
        self.breed = breed    # instance variable
        self.age = age        # instance variable

    def bark(self):
        print(f"{self.name} says: Woof!")

    def info(self):
        print(f"{self.name} is a {self.breed}, {self.age} years old")

    def birthday(self):
        self.age += 1
        print(f"Happy Birthday {self.name}! You are now {self.age} years old")



# Creating Objects (instances) from the class
dog1 = Dog("Bruno", "Labrador", 3)
dog2 = Dog("Max", "Poodle", 5)
dog3= Dog("Bucket","Golden retriver",7)


dog1.bark()   # Bruno says: Woof!
dog2.bark()   # Max says: Woof!
dog1.info()   # Bruno is a Labrador, 3 years old
dog3.birthday()
