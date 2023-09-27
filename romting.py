
import random

hp = 100
key = 0
key_found = False
master_key_found = False

LR_searched = False
BR_searched = False
KIT_searched = False
DR_searched = False
SF_searched = False
B_searched = False
MB_searched = False

Door_locked = True

entity_position = "master bedroom"
entity_damage = random.randint(10, 20)

key_spawn = random.randint(1, 3)
master_key_spawn = random.randint(1, 3)


def maxhp():
    global hp
    if hp > 100:
        hp = 100

def move_entity():
    global entity_position
    possible_positions = ["hallway", "living room", "kitchen", "dining room", "second hallway", "bedroom", "master bedroom"]
    entity_position = random.choice(possible_positions)
    print(f"The entity moved to {entity_position}.")

def check_entity_collision(player_room):
    global hp, entity_position
    if entity_position == player_room:
        print("The entity is in the same room as you!")
        hp -= entity_damage
        print(f"You have {hp} hp left.")

def rom_0():
    print("You escaped!")
    exit()

def rom_1():
    global master_key_found, Door_locked
    if Door_locked == False:
        move_entity()
        check_entity_collision("hallway")
    print()
    print("You're in the hallway.")
    ask = True
    while ask:
        print()
        valg = input("Type 1 to search the hallway. \nType 2 to go to the living room. \nType 3 to leave. \n-> ").upper()
        if valg == "1":
            print("You searched the hallway and found nothing.")
        elif valg == "2":
            ask = False
            rom_2()
        elif valg == "3":
            if master_key_found == True:
                print("You unlocked the door.")
                ask = False
                rom_0()
            if master_key_found == False:
                print("You need a master key to unlock this door.")
def rom_2():
    global key_spawn, LR_searched, key_found, Door_locked
    if Door_locked == False:
        move_entity()
        check_entity_collision("living room")
    print()
    print("You're in the living room.")
    ask = True
    while ask:
        print()
        valg = input("Type 1 to search the living room. \nType 2 to go to the hallway. \nType 3 to go to the kitchen. \nType 4 to go to the dining room. \n-> ").upper()
        if valg == "1":
            if LR_searched == True:
                print()
                print("You have already searched the living room.")


            else:
                if key_spawn == 1:
                    print()
                    print("You searched the living room and found a key!")
                    key_found = True
                    LR_searched= True
                else:
                    print()
                    print("You searched the living room but found nothing.")
                    LR_searched = True


        elif valg == "2":
            print()
            print("You walk to the hallway.")
            ask = False
            rom_1()

        if valg == "3":
            print()
            print("You walk to the kitchen.")
            ask = False
            rom_3()

        if valg == "4":
            print()
            print("You walk to the dining room.")
            ask = False
            rom_5()
        

def rom_3():
    global key_spawn, KIT_searched, key_found, Door_locked
    if Door_locked == False:
        move_entity()
        check_entity_collision("kitchen")
    print()
    print("You're in the kitchen.")
    ask = True
    while ask:
        print()
        valg = input("Type 1 to search the kitchen. \nType 2 to go to the bathroom. \nType 3 to go to the living room. \n-> ").upper()
        if valg == "1":
            if KIT_searched == True:
                print()
                print("You have already searched the kitchen.")

            else:
                if key_spawn == 2:
                    print()
                    print("You searched the kitchen and found a key!")
                    key_found = True
                    KIT_searched = True
                else:
                    print()
                    print("You searched the kitchen but found nothing.")
                    KIT_searched = True

        elif valg == "2":
            print()
            print("You walk to the bathroom.")
            ask = False
            rom_4()

        if valg == "3":
            print()
            print("You walk to the living room")
            ask = False
            rom_2()


def rom_4():
    global key_spawn, BR_searched, key_found, Door_locked
    if Door_locked == False:
        move_entity()
        check_entity_collision("bathroom")
    print()
    print("You're in the bathroom.")
    ask = True
    while ask:
        print()
        valg = input("Type 1 to search the bathroom. \nType 2 to go back to the kitchen. \n->").upper()

        if valg == "1":
            if BR_searched == True:
                print()
                print("You have already searched the bathroom.")

            else:
                if key_spawn == 3:
                    print()
                    print("You searched the bathroom and found a key!")
                    key_found = True
                    BR_searched = True
                else:
                    print()
                    print("You searched the bathroom but found nothing.")
                    BR_searched = True
        
        elif valg == "2":
            print()
            print("You went back into the kitchen.")
            rom_3()

def rom_5():
    global DR_searched, Door_locked, key_found, Door_locked
    if Door_locked == False:
        move_entity()
        check_entity_collision("dining room")
    print()
    print("You're in the dining room.")
    ask = True
    while ask:
        print()
        valg = input("Type 1 to search the dining room. \nType 2 to go up the stairs. \nType 3 to go to the living room. \n-> ").upper()
        if valg == "1":
            print()
            print("You searched the dining room and found nothing.")

        elif valg =="2":
            if Door_locked == True:
                if key_found == True:
                    print()
                    print("You unlocked the door to the second floor stairs.")
                    Door_locked = False
                    ask = False
                    rom_6()
                elif key_found == False:
                    print()
                    print("You dont have a key to this door.")
            if Door_locked == False:
                ask = False
                rom_6()
        elif valg =="3":
            print()
            print("You went to the living room.")
            ask = False
            rom_2()

def rom_down():
    print()
    print("You went down the stairs.")
    rom_5()

def rom_6():
    print()
    print("You went up the stairs.")
    rom_7()

def rom_7():
    global SF_searched, master_key_spawn, master_key_found, Door_locked
    if Door_locked == False:
        move_entity()
        check_entity_collision("second hallway")
    print()
    print("You're now in the second floor hallway.")
    ask = True
    while ask:
        print()
        valg = input("Type 1 to search the second floor hallway. \nType 2 to go down the stairs. \nType 3 to go to the bedroom. \nType 4 to go to the master bedroom. \n-> ").upper()
        if valg == "1":
            if SF_searched == True:
                print()
                print("You have already searched the hallway.")


            else:
                if master_key_spawn == 1:
                    print()
                    print("You searched the hallway and found the master key, you can now leave the house!")
                    master_key_found = True
                    SF_searched= True
                else:
                    print()
                    print("You searched the hallway but found nothing.")
                    SF_searched = True
        elif valg == "2":
            ask = False
            rom_down()
        elif valg == "3":
            ask = False
            print()
            print("You went to the bedroom.")
            rom_9()
        elif valg == "4":
            ask = False
            print()
            print("You went to the master bedroom.")
            rom_10()
            
        elif valg == "HERE":
            ask = False
            rom_8()

def rom_8():
    print()
    print("You're in the attic.")
    print("✋︎ 💧︎☜︎☜︎ ✡︎⚐︎🕆︎")
    rom_0()


def rom_9():
    global B_searched, master_key_spawn, master_key_found, Door_locked
    if Door_locked == False:
        move_entity()
        check_entity_collision("bedroom")
    print()
    print("You're in the bedroom.")
    ask = True
    while ask:
        valg = input("Type 1 to search the bedroom. \nType 2 to go to the second floor hallway. \n-> ")
        if valg == "1":
            if B_searched == True:
                print()
                print("You have already searched the bedroom.")
            else:
                if master_key_spawn == 2:
                    print()
                    print("You searched the bedroom and found the master key, you can now leave the house!")
                    master_key_found = True
                    B_searched= True
                else:
                    print()
                    print("You searched the bedroom but found nothing.")
                    B_searched = True
        elif valg == "2":
            print("You went back to the hallway.")
            ask = False
            rom_7()

def rom_10():
    global MB_searched, master_key_spawn, master_key_found, Door_locked
    if Door_locked == False:
        move_entity()
        check_entity_collision("master bedroom")
    print()
    print("You're in the master bedroom.")
    ask = True
    while ask:
        valg = input("Type 1 to search the master bedroom. \nType 2 to go to the second floor hallway. \nType 3 to go into the walk-in closet. \n-> ")
        if valg == "1":
            if MB_searched == True:
                print()
                print("You have already searched the master bedroom.")
            else:
                if master_key_spawn == 3:
                    print()
                    print("You searched the master bedroom and found the master key, you can now leave the house!")
                    master_key_found = True
                    MB_searched= True
                else:
                    print()
                    print("You searched the master bedroom but found nothing.")
                    MB_searched = True
        elif valg == "2":
            print("You went back to the hallway.")
            ask = False
            rom_7()
        elif valg == "3":
            print("You hid in the walk-in closet.")
            ask = False
            rom_11()

def rom_11():
    global Door_locked
    if Door_locked == False:
        move_entity()
    print("You're in the walk-in closet.")
    ask = True
    while ask:
        valg = input("Type 1 to keep hiding in the walk-in closet. \nType 2 to go back into the master bedroom. \n-> ")
        if valg == "1":
            print("You keep hiding in the walk-in closet.")
        elif valg == "2":
            print("You went back into the master bedroom.")
            ask = False
            rom_10()


def game_over():
    print("YOU DIED.")
    respawn()

def respawn():
    global hp
    hp = 100
    valg = input("Respawn? 1 = YES. 2 = NO -> ").upper()
    if valg == "1":
        rom_1()

    if valg == "2":
        exit()

rom_1()