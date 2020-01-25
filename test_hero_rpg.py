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

screen_with = 100


""" HERO  SETUP """

class Player():
    def __init__(self, name):
        self.name = name
        self.max_health_points = 100
        self.health_points = self.max_health_points
        self.attack = 20
        self.gold = 0
        self.potions = 0
        self.game_over = False
PlayerIG = Player(Player)

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
        self.max_health_points = 70
        self.health_points = self.max_health_points
        self.attack = 5
        self.gold_gain = 50
ZombieIG = Zombie('Zombie')

""" MAIN TITLE SCREEN """

def title_screen():
    os.system('clear')                       #Calling a command from the OS that clears the terminal after each section to reduce clutter. 
    print('############################')
    print('#                          #')
    print('#    Welcome Brave One!    #')
    print('#                          #')
    print('############################')
    print('#                          #')
    print('#     -- Start Game --     #')
    print('#       - Quit Game -      #')
    print('#                          #')
    print('#                          #')
    print('#                          #')
    print('#  Type Start Game, etc... #')
    print('############################')
    print('                            ')
    option = input('> ')                        # Using > to mark input area for player.
    if option.lower() == ('start game'):        #Using if, elif & while as conditions settings for the title screen.
        setup_game() 
    elif option.lower() == ('quit game'):
        sys.exit()
    else:
        title_screen()

""" START OPTION Q & A for gaining character info from player & Greeting the character """ #06:14/13:51 Part 5

def setup_game():
    os.system('clear')
    print("Hello. You seem new to these parts. What is your name stranger?")
    option = input('> ')
    global PlayerIG
    PlayerIG = Player(option)
    setup_game2()

def setup_game2():
    os.system('clear')
    print('"These are dark times brave one & we are in need of a person with your skills. Destroy the evil and become our hero." - Zartoes the Wise')
    print('')       
    print('')                                                            #The empty sets are act as pauses.  
    print('############################')
    print('#                          #')
    print('#    CHARACTER  SHEET      #')
    print('#                          #')
    print('############################')
    print('                            ')
    print('Hero\'s Name:    {}'.format(PlayerIG.name))
    print('Attack Power:    {}'.format(PlayerIG.attack))
    print('Health Points    {}/{}'.format(PlayerIG.max_health_points, PlayerIG.health_points))
    print('Gold Pieces:     {}'.format(PlayerIG.gold))
    print('Healing Potions: {}'.format(PlayerIG.potions))
    print('')
    print(' 1. Do Battle')                        
    print(' 2. Go to market')                         
    print(' 3. Exit Game')                           
    print('')
    print('Type 1, 2, or 3.')
    print('')
    option = input('> ')
    if option == '1':
        pre_fight()
    # elif option == '2':
    #     store()
    elif option == '3':
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
    print('#### {}            vs.        {} ####'.format(PlayerIG.name, enemy.name))
    print('')
    print('{}\'s Health: {}/{}           {}\'s Health: {}/{}'.format(PlayerIG.name, PlayerIG.max_health_points, PlayerIG.health_points, enemy.name, enemy.max_health_points, enemy.health_points))
    print('')
    print('Potions: {}'.format(PlayerIG.potions))
    print(' 1. Do Battle!') 
    print(' 2. Drink Postion') 
    print(' 3. Run Away!')  
    print('')
    option = input('> ')
    if option == '1':
        attack()
    elif option == '2':
        drink_potions()
    elif option == '3':
        run()
    else:
        fight()

def attack():
    os.system('clear')
    player_attack = random.randint(PlayerIG.attack / 2, PlayerIG.attack)
    enemy_attack = random.randint(enemy.attack / 2, enemy.attack)
    if player_attack == PlayerIG.attack / 2:
        print('You missed wildly!')
    else:
        enemy.health_points -= player_attack
        print('You hit the creature! {} damaged taken by the shawdow dweller!'.format(player_attack))
    option = input('')  #The empty sets are act as pauses. 
    if enemy.health_points <= 0:
        win()
    os.system('clear')
    if enemy_attack == enemy_attack / 2:
        print("The foul beast missed!")
    else:
        PlayerIG.health_points -= enemy_attack
        print("You have been wounded! {} damanged taken.".format(enemy_attack))
    option = input('')
    if PlayerIG.health_points <= 0:
        dead()
    else:
        fight()
    os.system('clear')

def drink_potions():
    os.system('clear')
    if PlayerIG.potions == 0:
        print("You out of luck! There is no potion left for you.")
    else:
        PlayerIG.health_points += 50
        if PlayerIG.health_points > PlayerIG.max_health_points:
            PlayerIG.health_points = PlayerIG.max_health_points
        print("The gods smile on you. You have a potion. You drink it and taste of nectar and spice but has a bitter after taste.")
    option = input ('') #The empty sets are act as pauses. 
    fight()

def run():
    os.system('clear')
    run_num = random.randint(1,4)
    if run_num ==  1:
        print("Your legs carry you away from the battle, but your heart died that they and your thoughts never left the battle field.")
        option = input ('')
        setup_game2()
    else:
        print("Your legs feel like dead weight. The hour of challenge is at hand. Stand your ground!!!")
        option = input ('')
        os.system('clear')
        enemy_attack = random.randint(enemy.attack /2, enemy.attack)
        if enemy_attack == enemy_attack /2:
            print("The foul beast missed!")
        else:
            PlayerIG.health_points -= enemy_attack
            print("You have been wounded! {} damanged taken.".format(enemy_attack))
        option = input('')
        if PlayerIG.health_points <= 0:
            dead()
        else:
            fight()
        os.system('clear')

def win():         
    os.system('clear')
    enemy.health_points = enemy.max_health_points
    PlayerIG.gold += enemy.gold_gain
    print('You have defeated the {} & have found {} gold pieces.'.format(enemy.name, enemy.gold_gain))
    option = input('')
    setup_game2()

def dead():
    os.system('clear')
    print('{} are no longer among the living. You are dead. My your soul no peace.'.format(PlayerIG.name))
    option = input ('')
    title_screen()



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
