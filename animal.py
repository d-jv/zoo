class Animal:
    def __init__(self, name, age, health, happiness):
        self.name = name
        self.age = age
        self.health = health
        self.happiness = happiness
        self.type = ''
    
    def display_info(self):
        print(f'Animal name: {self.name}\nAnimal age: {self.age} \nAnimal health: {self.health} \nAnimal happiness: {self.happiness} \nAnimal type: {self.type}')
        return self
    
    def feed(self):
        self.health += 10
        self.happiness += 10
        return self

class Mammals(Animal):
    def __init__(self, name, age, health, happiness):
        super().__init__(name, age, health, happiness)
        self.type = 'Mammal'

class Birds(Animal):
    def __init__(self, name, age, health, happiness):
        super().__init__(name, age, health, happiness)
        self.type = 'Bird'

class Reptiles(Animal):
    def __init__(self, name, age, health, happiness):
        super().__init__(name, age, health, happiness)
        self.type = 'Reptile'        

class Amphibians(Animal):
    def __init__(self, name, age, health, happiness):
        super().__init__(name, age, health, happiness)
        self.type = 'Amphibian'

class Insects(Animal):
    def __init__(self, name, age, health, happiness):
        super().__init__(name, age, health, happiness)
        self.type = 'Insect'
