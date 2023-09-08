print("Du går deg vill i en hule og lommelykta di begynner å gå tom for batteri.")
print("Batteriene blir tom etter 3 valg.")

valg = input("Hva gjør du? A: Gå videre inn og håp du finner nye batterier. B: Prøv å finn veien ut så fort som mulig. -> ")

if valg == "A":
    print("Du fortsetter videre inn i hulen i håp om å finne mye batterier")
    print("Du finner en sekk med 3 ting, en oljelampe, en lommekniv og batterier.")
    valg = input("Hva tar du? A: Oljelampen. B: Lommekniven. C: batteriene. D: Sekken.")

    if valg == "A":
        print("Du tok oljelampen, men du trenger noe å tenne den med. Det kommer noen bak deg og angriper deg, du har ingenting å beskytte deg med. DU DØDE.")
        
    if valg == "B":
        print("Du tok lommekniven. Det kommer noen bak deg og angriper deg, du bruker lommekniven i selv-forsvar og dreper monsteret.")
        print("Du fortsetter videre inn i hulen og håper på å finne en utvei.")

    if valg == "C":
        print("Du tok batteriene. Imens du er opptatt med å bytte batterier kommer det noen bak deg og angriper deg. DU DØDE.")

    if valg == "D":
        print("Du tok sekken. Det kommer noen bak deg og angriper deg, du hadde ikke tid til å hente lommekniven fra sekken. DU DØDE.")

elif valg == "B":
    print("Du ble stressa og begynte å løpe rundt i hulen, du gikk deg bare mere vill. Tiden du brukte på å løpe rundt gjorde sånn at det tok 2 valg.")
    print("Batteriene blir tom etter 1 valg")
    valg = input("Du må finne nye batterier, ellers blir du gal av mørket. A: Bli et med hulen. B: Dø.")

    if valg == "A":
        print("Du ga inn til hulen og skrudde av lommelykta.")
    
    if valg == "B":
        print("DU DØDE.")