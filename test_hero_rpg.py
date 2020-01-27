

name = "sean"
type(name)

""""""

#Sean Page

# In is a RPG game, the hero fights goblins and zombies. The player has the following options:
# 1. Fight a goblin or zombie. The fight encounters are randome.
# 2. Taking a health power potion which gives a random amount of health back to the hero.
# 3. Run away from the fight which can randomly result in either escape or staying in the fight anyway.
# 4. The hero can also got to a market to replace potions used in battle.
# 5. The hero can will also gain gold from downed creatures. 

import sys
import os
import textwrap
import time
import random
import fast



"""""""""""""
# def help_menu():
#     print('#########################')
#     print('#                       #')
#     print('#     - Help Menu -     #')
#     print('#                       #')
#     print('#########################')
#     print('                         ')
#     print('                         ')
#     print(' Stop asking for help &  ') #< Put game play instrutions here. Attack, Flee, Cast Magic, etc...
#     print('     play the game.      ') #< Put game play instrutions here. Attack, Flee, Cast Magic, etc...
#     print('                         ')
#     print('                         ')
#     print('                         ')
#     print('#########################')


    # for character in PlayerIG:
    # player_job = input('> ')
    # valid_jobs = ['warrior', 'mage', 'paladin']
    # if player_job.lower() in valid_jobs:
    #     myPlayer.job = player_job
    #     print("Great" + player + "!" "You have answered many prayers" + player_job + ".\n" )
    # while player_job.lower() not in valid_jobs:
    #     player_job = input('> ')
    #     if player_job.lower() in valid_jobs:
    #         myPlayer.job = player_job
    #         print("Great" + player_name + "!" "You have answered many prayers" + player_job + ".\n" )


# 
#  def setup_game():
#     question_1 = "Hello. You seem new to these parts. What is your name stranger?" #Add the \n since formating like this don't add a new line. 
#     for character in question_1:
#         sys.stdout.write(character)
#         sys.stdout.flush()
#         time.sleep(0.05)
#         player_name = input('> ')
#         myPlayer.name = player_name

#     question_2 = "These are dark times & we are in need of a person with skill. Are you a warrior, paladin or mage?\n"
#     for character in question_2:
#         sys.stdout.write(character)
#         sys.stdout.flush()
#         time.sleep(0.03)
#     player_job = input('> ')
#     valid_jobs = ['warrior', 'mage', 'paladin']
#     if player_job.lower() in valid_jobs:
#         myPlayer.job = player_job
#         print("Great" + player_name + "!" "You have answered many prayers" + player_job + ".\n" )
#     while player_job.lower() not in valid_jobs:
#         player_job = input('> ')
#         if player_job.lower() in valid_jobs:
#             myPlayer.job = player_job
#             print("Great" + player_name + "!" "You have answered many prayers" + player_job + ".\n" )


# #!/usr/bin/env python

# # In this simple RPG game, the hero fights the goblin. He has the options to:

# # 1. fight goblin
# # 2. do nothing - in which case the goblin will attack him anyway
# # 3. flee

# import sys
# import os

# import textwrap
# import time
# import random

# # screen_with = 100

# """ HERO SETUP """

# class hero:
#     def __init__(self, name):
#         self.name = ""
#         self.max_health = 0
#         self.power = 0
#         self.intimidation = []

# """ MAIN TITLE SCREEN """

# def title_screen():
#     print('##########################')
#     print('#                        #')
#     print('#     Welcome Hero!      #')
#     print('#                        #')
#     print('##########################')
#     print('#                        #')
#     print('#                        #')
#     print('#  Type 1 to Start Game  #')
#     print('#  Type 2 for Help Menu  #')
#     print('#  Type 3 to Quit Game   #')
#     print('#                        #')
#     print('#                        #')
#     print('##########################')

#     # def help_menu():
#     print('##########################')
#     print('#                        #')
#     print('#      -Help Menu -      #')
#     print('#                        #')
#     print('##########################')
#     print('                          ')
#     print('                          ')
#     print('                          ') #< Put game play instrutions here. Attack, Flee, Cast Magic, etc...
#     print('                          ') #< Put game play instrutions here. Attack, Flee, Cast Magic, etc...
#     print('                          ')
#     print('                          ')
#     print('                          ')
    
    # option = input('> ')                        # Using > to mark input area for player.
    # if option() == (1):        #Using if, elif & while as a conditions settings for the title screen.
    #     start_game() #*****playholder until written*****
    # elif option() == (2):
    #     help_menu
    # elif option() == (3):
    #     sys.exit()
    # else: 
    #     print('  Please enter a valid command.')
    #     option = input('> ')                        #Gives a 2nd chance to enter input correctly before game exits.
    # if option() == (1):
    #     start_game() #*****playholder until written*****
    # elif option() == (2):
    #     help_menu
    # elif option() == (3):
    #     sys.exit()

""" START OPTION Q & A (For gaining character info from player.) """

# def start_game():
#     print("You seem new to these parts. What is your name great warrior?")
#     option = input('> ')        #Option is what the the player types in.
#     global hero_type            #Placed global here so this can be used out this local function.
#     hero_type = hero(option)
#     start_question_1()

# def start_question_1():
#     print(f"Hello %d. It's nice to meet you my friend, even in these dark times.") % hero_type.now      #***** Redo in f'string. *****



# """ Example From GitHub """
#     main()
    

#     # hero.health() 
#     # hero.power()
#     # goblin.health()
#     # goblin.power()

# class Goblin:
#     def __init__(self, health, power):
#         goblin.health = goblin_health
#         goblin.power = goblin_power



# def main():
#     hero_health = 10
#     hero_power = 5
#     goblin_health = 6
#     goblin_power = 2

#     while goblin_health > 0 and hero_health > 0:
#         print("You have {} health and {} power.".format(hero_health, hero_power))
#         print("The goblin has {} health and {} power.".format(goblin_health, goblin_power))
#         print()
#         print("What do you want to do?")
#         print("1. fight goblin")
#         print("2. do nothing")
#         print("3. flee")
#         print("> ", end=' ')
#         raw_input = input()
#         if raw_input == "1":
#             # Hero attacks goblin
#             goblin_health -= hero_power
#             print("You do {} damage to the goblin.".format(hero_power))
#             if goblin_health <= 0:
#                 print("The goblin is dead.")
#         elif raw_input == "2":
#             pass
#         elif raw_input == "3":
#             print("Goodbye.")
#             break
#         else:
#             print("Invalid input {}".format(raw_input))

#         if goblin_health > 0:
#             # Goblin attacks hero
#             hero_health -= goblin_power
#             print("The goblin does {} damage to you.".format(goblin_power))
#             if hero_health <= 0:
#                 print("You are dead.")

# main()
