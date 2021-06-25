from animal import *


class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.zoo_name = zoo_name
    
    # Add mammals
    def add_lion(self, lion_name, age):
        self.animals.append(Mammals(lion_name, age, health=20, happiness=34))
        return self
    def add_kangaroo(self, kang_name, age):
        self.animals.append(Mammals(kang_name, age, health=61, happiness=25))
        return self
    
    # Add Birds
    def add_chicken(self, chicken_name, age):
        self.animals.append(Birds(chicken_name, age, health=51, happiness=44))
        return self
    def add_penguin(self, penguin_name, age):
        self.animals.append(Birds(penguin_name, age, health=76, happiness=54))
        return self
    
    # Add Reptilian
    def add_turtle(self, turtle_name, age):
        self.animals.append(Reptiles(turtle_name, age, health=51, happiness=44))
        return self
    def add_crocodile(self, croco_name, age):
        self.animals.append(Reptiles(croco_name, age, health=76, happiness=54))
        return self

    # Add Amphibians
    def add_frog(self, frog_name, age):
        self.animals.append(Amphibians(frog_name, age, health=80, happiness=76))
        return self
    def add_salamander(self, salamander_name, age):
        self.animals.append(Amphibians(salamander_name, age, health=40, happiness=34))
        return self

    # Add Insect
    def add_ant(self, ant_name, age):
        self.animals.append(Insects(ant_name, age, health=92, happiness=62))
        return self
    def add_caterpillar(self, caterpillar_name, age):
        self.animals.append(Insects(caterpillar_name, age, health=64, happiness=67))
        return self


    # Show the list of animals in Zoo 
    def print_all_info(self):
        print("-"*30, self.zoo_name, "-"*30)
        for i, animal in enumerate(self.animals, start=1):
            print(f'[{i}]')
            animal.display_info()
            print('-'*25)
        print("-"*25, f'End of list - {self.zoo_name}', "-"*25, '\n')
        return self