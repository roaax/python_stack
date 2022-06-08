from re import L


class Zoo:
    animals=[]
    def __init__(self, zoo_name , age , hp, hl):
        self.animals = []
        self.name = zoo_name
        self.age = 0
        self.hp = hl
        self.hl= hp

    def add_lion(self, name):
        self.animals.append( Lion(name) )

    def add_tiger(self, name):
        self.animals.append( Tiger(name) )

    def print_all_info(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            animal.display_info()

    def display_info(self):
        print(f"Name: {self.name} | Health Level: {self.hp} | Happieness Level: {self.hl} Feed: { feed(self.amount)}")
    
    def feed(self,amount):
        for x in range(amount):
            self.hp = self.hp+10
            self.hl = self.hl+10
        return self


class Lion(Zoo):
    def __init__(self, zoo_name,speed=100):
        super().__init__(zoo_name, age=20 , hp=300 , hl=95)
        self.speed=speed
        
class Tiger(Zoo):
    def __init__(self, zoo_name,):
        super().__init__(zoo_name, age=14 , hp=350 , hl=100)
        
        
class Bear(Zoo):
    def __init__(self, zoo_name,):
        super().__init__(zoo_name, age=10 , hp=150 , hl=80)
        

lion = Lion("Lions")
lion.add_lion("Nala")
lion.add_lion("Simba")
tiger= Tiger("Tigers")
tiger.add_tiger("Rajah")
tiger.add_tiger("Shere Khan")
print(lion.feed(40))
bear= Tiger("Tigers")
tiger.add_tiger("Rajah")
tiger.add_tiger("Shere Khan")
lion.print_all_info()
tiger.print_all_info()
