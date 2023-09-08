
import random

hp = 100

def maxhp():
    global hp
    if hp > 100:
        hp = 100

def rom_1():
    print("Du er i rom 1.")
    valg = input("Skriv A for å gå til rom 2, eller B for å gå til rom 3. -> ").upper()
    if valg == "A":
        rom_2()

    if valg == "B":
        rom_3()

def rom_2():
    global hp
    print("Du er i rom 2.")

    rando = random.randint(1, 5)
    if rando == 1:
        print("Du datt ned en trapp og fikk skrubbsår på kneet.")
        hp -=50
        print("Du har nå", hp, "liv igjen.")
    else:
        print("Du gikk ned en trapp og ingenting skjedde.")
        
    if hp <= 0:
        game_over()

    valg = input("Skriv A for å gå til rom 3, eller B for å tilbake til rom 1. -> ").upper()
    if valg == "A":
        rom_3()

    if valg == "B":
        rom_1()

def rom_3():
    global hp
    print("Du er i rom 3.")
    rando = random.randint(1, 5)
    if rando == 1:
        print("Du fant noen bandasjer og vant livet")
        hp +=20
        maxhp()
        print("Du har nå", hp, "liv igjen")
        
    else:
        print("Du skjekket en skuff og fant ingenting.")


    valg = input("Skriv A for å gå tilbake til rom 1, eller B for å gå tilbake til rom 2. -> ").upper()
    if valg == "A":
        rom_1()

    if valg == "B":
        rom_2()

def game_over():
    print("DU DØDE.")
    respawn()

def respawn():
    global hp
    hp = 100
    valg = input("Respawn? A = JA. B = NEI -> ").upper()
    if valg == "A":
        rom_1()

    if valg == "B":
        exit()
        
rom_1()