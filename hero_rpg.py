# Sean Page
# Week 2,01/27/20
# Python Project, Text Based RPG Game 

# In is a RPG game, the hero fights goblins and zombies. The hero has the following options:
# 1. Fight a goblin or zombie. The fight encounters are random.
# 2. Run away from the fight which can randomly result in either escape or staying in the fight anyway. The hero may be hit while attempting to run.
# 3. The hero can also gain gold from downed creatures. I subbed gold for power because what's an rpg without gold?!

import sys         #sys — System-specific parameters and functions. This module provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter.
import os          #The OS module in python provides functions for interacting with the operating system. OS, comes under Python's standard utility modules. This module provides a portable way of using operating system dependent functionality.
import textwrap
import time
import random

screen_with = 100

""" HERO & ENEMY SETUP """
                                        #Notes:
class hero():                           #Classes allow the programer to initialize & store the state of the values so that it can be accessed later in the program. 
    def __init__(self, name):           #A class defines the general behavior that a whole category of objects can follow & the info can be associated with those objects.     
        self.name = name                # the __init__ is a constructor method. The info in the () are objects (aka parameters. The objects have... 
        self.max_health_points = 100    #...attributes attached to them. In this example those attributes such as name, max_health_points, attack, etc..
        self.health_points = self.max_health_points
        self.attack = 20
        self.gold = 0
        self.game_over = False
heroIG = hero(hero)   #heroIG is a variable sets a new instance of the class hero. It invokes the class hero() & has all of its attributes.           
                                        #Example:  class Hero()""
class Goblin():                                     #    def __init__(self, name, max_health_points, health__points, attack, gold_gain)
    def __init__(self, name):                       #Goblin = Hero(self, name, max_health_points, health__points, attack, gold_gain)                                              
        self.name = name                            #Zombie = Hero(self, name, max_health_points, health__points, attack, gold_gain)    
        self.max_health_points = 30                  
        self.health_points = self.max_health_points
        self.attack = 10
        self.gold_gain = 10
GoblinIG = Goblin('Goblin')

class Zombie():
    def __init__(self, name):
        self.name = name
        self.max_health_points = 150
        self.health_points = self.max_health_points
        self.attack = 10
        self.gold_gain = 50
ZombieIG = Zombie('Zombie')

""" MAIN TITLE SCREEN """

def title_screen():                          #Defined a new method and named it title_screen().
    os.system('clear')                       #Calls a command from the OS that clears the terminal after each section to reduce clutter. 
    print('##################################')
    print('#                                #')
    print('#       Welcome Brave One!       #')
    print('#                                #')
    print('##################################')
    print('#                                #')
    print('#        -- Start Game --        #')
    print('#         - Quit Game -          #')
    print('#                                #')
    print('#                                #')
    print('#                                #')
    print('#  Type Start Game or Quit Game  #')
    print('##################################')
    print('                                  ')
    option = input('> ')                        # Using > to mark input area for hero.
    if option.lower() == ('start game'):        # Using if, elif & while as conditions settings for the title screen.
        setup_game()                            #.lower method will make everthing lower so capitalization want create an error. 
    elif option.lower() == ('quit game'):
        sys.exit()                              
    else:
        title_screen()

""" START OPTION Q & A for gaining character info & greeting the character """

def setup_game():
    os.system('clear')                        # Clears the screen to reduce clutter. 
    print("Hello. You seem new to these parts. What is your name stranger?")
    option = input('> ')
    global heroIG               #Global variable.
    heroIG = hero(option)
    setup_game2()

def setup_game2():
    os.system('clear')
    print('"These are dark times brave one & we are in need of a person with your skills. -  Book of Zartoes the Wise"')
    print('"Destroy the evil and become our hero." - Book of the Brave One"')       
    print('')                                     
    print('############################')
    print('#                          #')
    print('#    CHARACTER  SHEET      #')
    print('#                          #')
    print('############################')
    print('                            ')
    print('Hero\'s Name:    {}'.format(heroIG.name))    #These could have been f'strings. print(f'Hero\'s Name: {heroIG.name}')
    print('Attack Power:    {}'.format(heroIG.attack))
    print('Health Points:   {}/{}'.format(heroIG.max_health_points, heroIG.health_points))
    print('Gold Pieces:     {}'.format(heroIG.gold))
    print('')
    print(' 1. Do Battle!') 
    print('')               
    print(' 2. Exit Game.')                           
    print('')
    print( 'Type 1 or 2 & press enter.')
    print('')
    option = input('> ')
    if option == '1':                         #The logic for the the character sheet. 
        pre_fight()           #Could have used a while loop. Example, while option != '1' and option != '2:
    elif option == '2':                                                 #set_game2()
        sys.exit()              #if a while loop was used I would have created a def option_picked with if & elif with their perspective call paths.
    else:
        setup_game2()

""" COMBAT """

def pre_fight():                        
    global enemy
    enemy_number = random.randint(1,2)
    if enemy_number == 1:
        enemy = GoblinIG
    else:
        enemy = ZombieIG
    fight()

def fight():
    os.system('clear')
    print('#### {}            vs.        {} ####'.format(heroIG.name, enemy.name))
    print('')
    print('{}\'s Health: {}/{}           {}\'s Health: {}/{}'.format(heroIG.name, heroIG.max_health_points, heroIG.health_points, enemy.name, enemy.max_health_points, enemy.health_points))
    print('')
    print(' 1. Fight!') 
    print('')
    print(' 2. Run Away.')  
    print('')
    option = input('> ')
    if option == '1':
        attack()
    elif option == '2':
        run()
    else:
        fight()

def attack():
    os.system('clear')
    hero_attack = random.randint(heroIG.attack - 2, heroIG.attack) #Lowest attack will have 2 subtracted from it and the hightest attack will be unchanged.
    enemy_attack = random.randint(enemy.attack - 2, enemy.attack)
    if hero_attack == heroIG.attack - 2:                           
        print('You missed wildly!')
    else:
        enemy.health_points -= hero_attack                         #This takes the enemy health and has the hero attack subtract from it.
        print('You hit the creature! {} damaged taken by the shawdow dweller!'.format(hero_attack))
    option = input('')       #This empty set acts as pauses.       #Once the enemy's health get to or less than 0 the code go to the win(), code runs and displays that the player won.
    if enemy.health_points <= 0:
        win()
    os.system('clear')
    if enemy_attack == enemy_attack - 2:
        print("The foul beast missed!!")
    else:
        heroIG.health_points -= enemy_attack
        print("The creature strikes and you have been wounded! Blood flows from your injury. {} damanged taken.".format(enemy_attack))
    option = input('')
    if heroIG.health_points <= 0:
        dead()
    else:
        fight()
    os.system('clear')

def run():
    os.system('clear')
    run_num = random.randint(1,4)    
    if run_num ==  1:               
        print("Your legs carry you away from the battle, but your heart died that day and your thoughts never left the battle field.")
        option = input ('')
        setup_game2()
    else:
        print("Your legs feel like dead weight. The hour of challenge is at hand. Stand your ground!!!")
        option = input ('')
        os.system('clear')
        enemy_attack = random.randint(enemy.attack - 2, enemy.attack)
        if enemy_attack == enemy_attack - 2:
            print("The foul beast missed!")
        else:
            heroIG.health_points -= enemy_attack
            print("You have been wounded! {} damanged taken.".format(enemy_attack))
        option = input('')
        if heroIG.health_points <= 0:
            dead()
        else:
            fight()
        os.system('clear')

def win():         
    os.system('clear')
    enemy.health_points = enemy.max_health_points
    heroIG.gold += enemy.gold_gain
    print('                ### Sweet Victory! ###')
    print('                      ')
    print('You have defeated the {} & have found {} gold pieces.'.format(enemy.name, enemy.gold_gain))
    option = input('')
    setup_game2()

def dead():
    os.system('clear')
    print('                      ')
    print('                                +++GAME OVER+++')
    print('                      ')
    print('{} is no longer among the living. You are dead. May your soul know peace.'.format(heroIG.name))
    option = input ('')
    sys.exit()


title_screen()                  