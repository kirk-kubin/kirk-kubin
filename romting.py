
import random

hp = 100
key = 0
key_found = False
stairs_key = 0

LR_searched = False
BR_searched = False
KIT_searched = False
DR_searched = False

Door_locked = True

entity_position = "outside"
entity_damage = 10

key_spawn = random.randint(1, 3)


def maxhp():
    global hp
    if hp > 100:
        hp = 100

def move_entity():
    global entity_position
    possible_positions = ["hallway", "living room", "kitchen", "dining room"]
    entity_position = random.choice(possible_positions)
    print(f"The entity moved to {entity_position}.")

def check_entity_collision(player_room):
    global hp, entity_position
    if entity_position == player_room:
        print("The entity is in the same room as you!")
        hp -= entity_damage

def rom_1():
    print("You're in the hallway.")
    ask = True
    while ask:
        valg = input("Type A to search the hallway. Type B to go to the living room. -> ").upper()
        if valg == "A":
            print("You searched the hallway and found nothing.")
        elif valg == "B":
            ask = False
            rom_2()

def rom_2():
    global key_spawn, LR_searched, key_found
    print("You're in the living room.")
    ask = True
    while ask:
        valg = input("Type A to search the living room. Type B to go to the hallway. Type C to go to the kitchen. Type D to go to the dining room. -> ").upper()
        if valg == "A":
            if LR_searched == True:
                print("You have already searched the living room.")


            else:
                if key_spawn == 1:
                    print("You searched the living room and found a key!")
                    key_found = True
                    LR_searched= True
                else:
                    print("You searched the living room but found nothing.")
                    LR_searched = True


        elif valg == "B":
            print("You walk to the hallway.")
            ask = False
            rom_1()

        if valg == "C":
            print("You walk to the kitchen.")
            ask = False
            rom_3()

        if valg == "D":
            print("You walk to the dining room.")
            ask = False
            rom_5()
        

def rom_3():
    global key_spawn, KIT_searched, key_found
    print("You're in the kitchen.")
    ask = True
    while ask:

        valg = input("Type A to search the kitchen. Type B to go to the bathroom. Type C to go to the living room. -> ").upper()
        if valg == "A":
            if KIT_searched == True:
                print("You have already searched the kitchen.")

            else:
                if key_spawn == 2:
                    print("You searched the kitchen and found a key!")
                    key_found = True
                    KIT_searched = True
                else:
                    print("You searched the kitchen but found nothing.")
                    KIT_searched = True

        elif valg == "B":
            print("You walk to the bathroom.")
            ask = False
            rom_4()

        if valg == "C":
            print("You walk to the living room")
            ask = False
            rom_2()


def rom_4():
    global key_spawn, BR_searched, key_found
    print("You're in the bathroom.")
    ask = True
    while ask:
        valg = input("Type A to search the bathroom. Type B to go back to the kitchen. ->").upper()

        if valg == "A":
            if BR_searched == True:
                print("You have already searched the bathroom.")

            else:
                if key_spawn == 3:
                    print("You searched the bathroom and found a key!")
                    key_found = True
                    BR_searched = True
                else:
                    print("You searched the bathroom but found nothing.")
                    BR_searched = True
            
        elif valg == "B":
            print("You went back into the kitchen.")
            rom_3()

def rom_5():
    global DR_searched, Door_locked, key_found
    print("You're in the dining room.")
    ask = True
    while ask:
        valg = input("Type A to search the dining room. Type B to unlock the stairs door. Type C to go to the living room. -> ").upper()

        if valg == "A":
            print("You searched the dining room and found nothing.")

        elif valg =="B":
            if Door_locked == True:
                if key_found == True:
                    print("You unlocked the door to the second floor stairs.")
                    Door_locked = False
                    ask = False
                    rom_6()
                elif key_found == False:
                    print("You dont have a key to this door.")
            if Door_locked == False:
                ask = False
                rom_6()
def rom_6():
    print("You went up the stairs.")
    input()
    rom_7()

def rom_7():
    print("You're now on the second floor.")
    ask = True
    while ask:
        valg = input("Type A to search the second floor. Type B to go down the stairs. Type C to go to the bedroom. Type D to go to the master bedroom. -> ").upper()
        if valg == "A":
            print("You searched the second floor and found nothing.")
        elif valg == "B":
            ask = False
            rom_8()


def rom_8():
    print("You're in the attic.")

def rom_9():
    print("You're in the bedroom.")

def rom_10():
    print("You're in the master bedroom.")

def rom_11():
    print("You're in the walk-in closet.")

def game_over():
    print("YOU DIED.")
    respawn()

def respawn():
    global hp
    hp = 100
    valg = input("Respawn? A = YES. B = NO -> ").upper()
    if valg == "A":
        rom_1()

    if valg == "B":
        exit()
        
rom_1()