
class Animal:
    def __init__(self, name, age, hl, hp ):
        self.name=name
        self.age=age
        self.health_level=hl
        self.happiness_level=hp

    def feed(self, health, happiness):
        self.health_level+=health
        self.happiness_level+=happiness
        return(self)

    def display_info(self):
        print(f"Animal is: {self.type} \nName: {self.name} | Health level: {self.health_level} | Happiness level: {self.happiness_level} | {self.unique} \n " , "-"*65)

class Cheetah (Animal):
    def __init__(self, name):
        super().__init__(name, age=15, hl=90, hp=90)
        self.type="Cheetah"
        self.unique= "Features : speed is 130km/h"

    def feed(self):
        super().feed(health=91, happiness=95)

class Deer(Animal):
    def __init__(self, name):
        super().__init__(name, age=20 , hl=50, hp=60)
        self.type="Deer"
        self.unique = "Features : Antlers"

    def feed(self):
        super().feed(health=60, happiness=30)

class Crocodile(Animal):
    def __init__(self, name):
        super().__init__(name, age=25 , hl=80, hp=60)
        self.type="Crocodile"
        self.unique= "Features : Skin" 

    def feed(self):
        super().feed(health=80, happiness=700)

Blaze = Cheetah("Blaze")
Sandy = Deer("Sandy")
Derek = Crocodile("Derek")
