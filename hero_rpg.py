#Sean Page
#Week 2, Python Project

# In is a RPG game, the hero fights goblins and zombies. The hero has the following options:
# 1. Fight a goblin or zombie. The fight encounters are random.
# 2. Run away from the fight which can randomly result in either escape or staying in the fight anyway. The hero may be hit while attempting to run.
# 3. The hero can also gain gold from downed creatures. I subbed gold for power because what's an rpg without gold?!

import sys
import os
import textwrap
import time
import random

screen_with = 100

""" HERO & ENEMY SETUP """

class hero():
    def __init__(self, name):
        self.name = name
        self.max_health_points = 100
        self.health_points = self.max_health_points
        self.attack = 20
        self.gold = 0
        self.game_over = False
heroIG = hero(hero)

class Goblin():
    def __init__(self, name):
        self.name = name
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

def title_screen():
    os.system('clear')                       #Calling a command from the OS that clears the terminal after each section to reduce clutter. 
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
        setup_game() 
    elif option.lower() == ('quit game'):
        sys.exit()
    else:
        title_screen()

""" START OPTION Q & A for gaining character info & greeting the character """

def setup_game():
    os.system('clear')                        # Clears the screen to reduce clutter. 
    print("Hello. You seem new to these parts. What is your name stranger?")
    option = input('> ')
    global heroIG
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
    print('Hero\'s Name:    {}'.format(heroIG.name))
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
    if option == '1':
        pre_fight()
    elif option == '2':
        sys.exit()
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
    hero_attack = random.randint(heroIG.attack - 2, heroIG.attack)
    enemy_attack = random.randint(enemy.attack - 2, enemy.attack)
    if hero_attack == heroIG.attack - 2:
        print('You missed wildly!')
    else:
        enemy.health_points -= hero_attack
        print('You hit the creature! {} damaged taken by the shawdow dweller!'.format(hero_attack))
    option = input('')  #This empty set acts as pauses. 
    if enemy.health_points <= 0:
        win()
    os.system('clear')
    if enemy_attack == enemy_attack - 2:
        print("The foul beast missed!!")
    else:
        heroIG.health_points -= enemy_attack
        print("You have been wounded! Blood flows from your injury. {} damanged taken.".format(enemy_attack))
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
    print('{} are no longer among the living. You are dead. May your soul know peace.'.format(heroIG.name))
    option = input ('')
    title_screen()             #change this to sys.exit() so game exits. Right now it starts player back at title_screen with full health but the enemies have same health from the last fight.


title_screen()                  #Not sure why I need title_screen() back to back. If I remove either one it does not work. 