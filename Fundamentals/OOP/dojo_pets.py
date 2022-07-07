class Ninja:
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self. pet_food = pet_food
        self.pet = pet
    
    def walk(self):
        self.pet.play()
        print("Did you have fun?")

        return self

    def feed(self):
        self.pet.eat()
        print("Enjoy your food!")

        return self

    def bathe(self):
        self.pet.noise()
        print("Now you're all clean!")
        self.pet.sleep()

        return self

class Pet:
    def __init__(self, name, type, tricks):
        self.name = name
        self.type = type
        self.tricks = tricks

        self.health = 100
        self.energy = 100
    
    def sleep(self):
        if (self.energy+25) <= 100:
            self.energy += 25
    
    def eat(self):
        if (self.energy+5) <= 100:
            self.energy += 5
        if (self.health+10) <= 100:
            self.health += 10

    def play(self):
        if (self.health-10) >= 0:
            self.health -= 10
        if (self.energy-20) >= 0:
            self.health -= 20
    
    def noise(self):
        print("~noise!~")


ninja1_pet = Pet("ninja1's pet", "sloth", "sleep")
ninja1 = Ninja("coding", "master", "leaves", "grass", ninja1_pet)

ninja1.feed()
ninja1.walk()
ninja1.bathe()