from datetime import datetime, time
from zoo import *


zoo1 = Zoo('Zoo 014')

def greetings():
    user_name = input('Please enter your username: ')
    print(f'You have successfully logged in as {user_name}')
    return user_name

def main():
    while True:
        keep = stayInside()
        if keep == '5': # Exit
            now = datetime.now()
            now_time = now.time()
            if now_time >= time(19,00) or now_time <= time(6,00):
                dayOrNight = 'night'
            else: 
                dayOrNight = 'day'        
            print(f'\nGoodbye {user_name}. Have a nice {dayOrNight}!')
            break
        elif keep == '1': # Add animal
            whatAnimal()
        elif keep == '2': # Feed animal
            whatAnimalToFeed()
        elif keep == '3': # Delete animal
            pass
        elif keep == '4': # Show current animal list
            printZooInfo()
        else:  # Testing
            print('hehehehehe')

def printZooInfo():
    zoo1.print_all_info()
    return

def stayInside():
    keep = input('\nWhat do you want to do?: \n1) Add animal\n2) Feed animal\n3) Delete animal\n4) Show current animal list\n5) Exit.\nYour option: ')
    while keep not in ('1','2','3','4','5'):
        print('\nERROR. Please choose a valid option (1-2-3-4-5)\n')
        keep = input('\nWhat do you want to do?: \n1) Add animal\n2) Feed animal\n3) Delete animal\n4) Show current animal list\n5) Exit.\nYour option: ')
    return keep

def whatAnimal():
    typeAnimal = input('\nWhat type of animal?: \n1) Mammal\n2) Bird\n3) Reptilian\n4) Amphibian\n5) Insect\n6) Back.\nYour option: ')
    while typeAnimal not in ('1','2','3','4','5','6'):
        print('\nERROR. Please choose a valid option (1-2-3-4-5-6)\n')
        typeAnimal = input('\nWhat type of animal?: \n1) Mammal\n2) Bird\n3) Reptilian\n4) Amphibian\n5) Insect\n6) Back.\nYour option: ')
    else:
        if typeAnimal == '6':
            return
        if typeAnimal == '1':
            mammal = input('\nChoose an animal: \n1) Lion \n2) Kangaroo \n3) Back.\nYour option: ')
            while mammal not in ('1','2','3'):
                print('\nERROR. Please choose a valid option (1-2-3)\n')
                mammal = input('\nChoose an animal: \n1) Lion \n2) Kangaroo \n3) Back.\nYour option: ')
            if mammal == '1':
                lion_name = input('Lion name: ')
                lion_age = input('Lion age: ')
                print('')
                zoo1.add_lion(lion_name, int(lion_age))
            if mammal == '2':
                kang_name = input('Kangaroo name: ')
                kang_age = input('Kangaroo age: ')
                print('')
                zoo1.add_kangaroo(kang_name, int(kang_age))
            if mammal == '3':
                whatAnimal()
        if typeAnimal == '2':
            bird = input('\nChoose an animal: \n1) Chicken \n2) Penguin \n3) Back.\nYour option: ')
            while bird not in ('1','2','3'):
                print('\nERROR. Please choose a valid option (1-2-3)\n')
                bird = input('\nChoose an animal: \n1) Chicken \n2) Penguin \n3) Back.\nYour option: ')
            if bird == '1':
                chicken_name = input('Chicken name: ')
                chicken_age = input('Chicken age: ')
                print('')
                zoo1.add_chicken(chicken_name, int(chicken_age))
            if bird == '2':
                penguin_name = input('Penguin name: ')
                penguin_age = input('Penguin age: ')
                print('')
                zoo1.add_penguin(penguin_name, int(penguin_age))
            if bird == '3':
                whatAnimal()
        if typeAnimal == '3':
            reptilian = input('\nChoose an animal: \n1) Turtle \n2) Crocodile \n3) Back.\nYour option: ')
            while reptilian not in ('1','2','3'):
                print('\nERROR. Please choose a valid option (1-2-3)\n')
                reptilian = input('\nChoose an animal: \n1) Turtle \n2) Crocodile \n3) Back.\nYour option: ')
            if reptilian == '1':
                turtle_name = input('Turtle name: ')
                turtle_age = input('Turtle age: ')
                print('')
                zoo1.add_turtle(turtle_name, int(turtle_age))
            if reptilian == '2':
                croco_name = input('Croco name: ')
                croco_age = input('Croco age: ')
                print('')
                zoo1.add_crocodile(croco_name, int(croco_age))
            if reptilian == '3':
                whatAnimal()
        if typeAnimal == '4':
            amphibian = input('\nChoose an animal: \n1) Frog \n2) Salamander \n3) Back.\nYour option: ')
            while amphibian not in ('1','2','3'):
                print('\nERROR. Please choose a valid option (1-2-3)\n')
                amphibian = input('\nChoose an animal: \n1) Frog \n2) Salamander \n3) Back.\nYour option: ')
            if amphibian == '1':
                frog_name = input('Frog name: ')
                frog_age = input('Frog age: ')
                print('')
                zoo1.add_frog(frog_name, int(frog_age))
            if amphibian == '2':
                salamander_name = input('Salamander name: ')
                salamander_age = input('Salamander age: ')
                print('')
                zoo1.add_salamander(salamander_name, int(salamander_age))
            if amphibian == '3':
                whatAnimal()
        if typeAnimal == '5':
            insect = input('\nChoose an animal: \n1) Ant \n2) Caterpillar \n3) Back.\nYour option: ')
            while insect not in ('1','2','3'):
                print('\nERROR. Please choose a valid option (1-2-3)\n')
                insect = input('\nChoose an animal: \n1) Ant \n2) Caterpillar \n3) Back.\nYour option: ')
            if insect == '1':
                ant_name = input('Ant name: ')
                ant_age = input('Ant age: ')
                print('')
                zoo1.add_ant(ant_name, int(ant_age))
            if insect == '2':
                caterpillar_name = input('Caterpillar name: ')
                caterpillar_age = input('Caterpillar age: ')
                print('')
                zoo1.add_caterpillar(caterpillar_name, int(caterpillar_age))
            if insect == '3':
                whatAnimal()

def whatAnimalToFeed():
    if len(zoo1.animals)>0:
        zoo1.print_all_info()
        # print(len(zoo1.animals))
        feedAnimal = int(input('\nEnter number of animal to feed (or 0 (zero) to go back): '))
        if feedAnimal != 0:
            if feedAnimal > len(zoo1.animals):
                print('\nERROR. Please choose a valid number\n')
                zoo1.print_all_info()
                print('')
                feedAnimal = input('Enter number of animal to feed: ')
            else:
                zoo1.animals[feedAnimal-1].feed()
                whatAnimalToFeed()
        else: return
    else: 
        print('\nERROR. Zoo without animals\n')
        return

user_name = greetings()
main()