import random

tall = random.randint(1,100)
tall = int(tall)

forsøk = 0
forsøk = int(forsøk)
#print(tall)

while True:
    
    svar = input("Gjett et tall mellom 1 og 100 -> ")
    svar = int(svar)

    if svar < tall:
        print("Høyere.")
    if svar > tall:
         print("Lavere.")
    if svar == tall:
        print("Riktig!")
    break

