from animals import Animal
from animals import Cheetah
from animals import Deer
from animals import Crocodile

class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name

    def add_Cheetah(self, name):
        self.animals.append(Cheetah(name) )

    def add_Deer(self, name):
        self.animals.append(Deer(name) )

    def add_Crocodil(self, name):
        self.animals.append(Crocodile(name) )

    def print_all_info(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            animal.display_info()

#lets add some animals to the zoo
zoo1 = Zoo("Riys's Zoo")
zoo1.add_Cheetah("Cleo")
zoo1.add_Cheetah("Rock")

zoo1.add_Deer("Nala")
zoo1.add_Deer("Toto")

zoo1.add_Crocodil("Flash")
zoo1.add_Crocodil("Frank")

zoo1.print_all_info()