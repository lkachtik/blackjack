from random import randrange
from os import system
from time import sleep

clear = lambda: system('cls')
clear()

print"===  BLACKJACK  ==="
print"Povolene prikazy:'ano', 'ne', cisla, 'help'.\n"

# ZADEFINOVANI KONSTANT NA UVOD
a = [2,3,4,5,6,7,8,9,10,"J","Q","K","A"]*4 # vytvori serazeny balicek karet
b = [] # zamichany balicek karet
u_p = 0  # hodnota karet hrace
pc_p = 0 # hodnota karet pocitace
otazka2 = "whatever"
vklad = 0
sazka = 0
ano = ("ano", "a", "yes", "y", "")
ne = ("ne", "no", "n")
pomoc = ("pomoc", "help", "about", "o hre")

o_hre = open("jak_to_asi_funguje.txt","r")
about = o_hre.read()
o_hre.close()

# ZJISTENI, JESLTI MA HRAC 18 LET  - V ZAVISLOSTI NA ODPOVEDI SE PROGRAM BUDE CHOVAT JINAK
while True:
    otazka = raw_input("Je ti 18 let a vice? ")
    otazka = otazka.lower()
    if otazka in ano:
        print"Protoze ti je vice nez 18, budes mit moznost sazet. Hodne stesti!"
        sleep(1)
        break
    elif otazka in ne:
        print"Hra pobezi v omezenm rezimu bez sazek. Hodne stesti!"
        sleep(1)
        break
    elif otazka in pomoc:
        print "\n" + about
        continue
    else:
        print"Napis prosim ano nebo ne."
        continue

# OTAZKA, KOLIK CHCE HRAC VLOZIT NA VKLAD
while otazka in ano:
    try:
        vklad = raw_input("Jak velky chces provest vklad? ")
        vklad = vklad.lower()
        if vklad in pomoc:
            print "\n" + about
            continue
        vklad = int(vklad)
        if vklad <= 0:
            print "Zadej prosim cele cislo vetsi nez 0."
            continue
        break
    except ValueError:
        print("Zadej prosim cele cislo.")
        continue

# ZAMICHA BALICEK KARET
for i in range(52): 
    x = randrange(0,52-i)
    b.append(a[x]) # vezme nahodnou kartu z balicku "a" a prida ji do balicku "b"
    del a[x] # odstrani danou kartu z balicku "a"
    # tohle se stane celkem 52x

# SMYCKA, KTERA BEZI, DOKUD NEREKNU, ZE UZ NECHCI HRAT
while otazka in ano or otazka in ne:
    
    if otazka in ano:    
        while True:
            try:
                sazka = raw_input("Kolik chces vsadit do dalsi hry? ")
                sazka = sazka.lower()
                if sazka in pomoc:
                    print "\n" + about
                    continue
                sazka = int(sazka)
                if sazka <= 0:
                    print "Zadej prosim cele cislo vetsi nez 0."
                    continue
                elif sazka > vklad:
                    print "Mas pouze " + str(vklad) + ". Zadej prosim mensi hodnotu."
                    continue
                break
            except ValueError:
                print("Zadej prosim cele cislo.")
                continue
    
    u_v = 0 # soucet bodu hrace
    pc_v = 0 # soucet bodu pocitace
    u_ace = 0 # pocet Es hrace v ruce
    pc_ace = 0 # pocet Es pocitace v ruce
    u_karty = [] # karty v ruce hrace
    pc_karty = [] # karty v ruce pocitace
    c = [] # karty na stole
    d = [] # zamichane karty ze stolu

    # TAHNE PRVNI KARTU PRO HRACE
    u = b[0] # vytahne prvni kartu z balicku
    u_karty.append(u) # vlozi ji uzivatelovi do ruky
    if u == "J" or u == "Q" or u == "K": # priradi hodnotam J, Q a K hodnotu 10
        u = 10
    if u == "A": # priradi Esu hodnotu 11
        u = 11
        u_ace += 1 # pocita, kolik ma hrac v ruce Es, aby jim pak pripadne mohl snizovat hodnotu z 11 na 1
    u_v += u # prida hodnotu karty k celkove hodnote vsech karet
    c.append(b[0]) # prida kartu mezi karty na stole
    del b[0] # odebere kartu z hraciho balicku
        
    # TAHNE PRVNI KARTU PRO POCITAC
    pc = b[0]
    pc_karty.append(pc)
    if pc == "J" or pc == "Q" or pc == "K": # vsechny karty vetsi nez 10 maji hodnotu 10
        pc = 10
    if pc == "A": # pocitadlo Es hrace
        pc = 11
        pc_ace += 1
    pc_v += pc
    c.append(b[0])
    del b[0]
    
    # TAHNE DRUOU KARTU PRO HRACE
    u = b[0] # vytahne prvni kartu z balicku
    u_karty.append(u) # vlozi ji uzivatelovi do ruky
    if u == "J" or u == "Q" or u == "K": # priradi hodnotam J, Q a K hodnotu 10
        u = 10
    if u == "A": # priradi Esu hodnotu 11
        u = 11
        u_ace += 1 # pocita, kolik ma hrac v ruce Es, aby jim pak pripadne mohl snizovat hodnotu z 11 na 1
    u_v += u # prida hodnotu karty k celkove hodnote vsech karet
    c.append(b[0]) # prida kartu mezi karty na stole
    del b[0] # odebere kartu z hraciho balicku
    
    # Jaka je pravdepodobnost, ze na zacatku dostanu 2 Esa? Mala, ale mne uz se to stalo a vypsalo mi to soucet 22, pfff.     
    if u_v > 21 and u_ace > 0: # +2 - podminka - pokud je muj soucet vetsi nez 21 a zaroven je jedna ma karta Eso, tak zmensit muj souect o 10
            u_v -= 10
            u_ace -=1
    
    n = len(u_karty)
    u_karty2 = ""
    for i in range(n):
        u_karty2 += str(u_karty[i]) + " "
        
    n = len(pc_karty)
    pc_karty2 = ""
    for i in range(n):
        pc_karty2 += str(pc_karty[i]) + " "

    print "Tve karty - " + str(u_karty2) + "- soucet: " + str(u_v)
    print "Karty pocitace - " +str(pc_karty2) + "- soucet:" + str(pc_v)    
    
    while True:
        u=raw_input("Chces dalsi kartu? ")
        u = u.lower()
        if u in pomoc:
            print "\n" + about
            continue
        if u in ano:
            u = b[0]
            u_karty.append(u)
            if u == "J" or u == "Q" or u == "K": # vsechny karty vetsi nez 10 maji hodnotu 10
                u = 10
            if u == "A": # pocitadlo Es hrace
                u = 11          
                u_ace += 1  
            u_v += u
            c.append(b[0])
            del b[0]
            if u_v > 21 and u_ace > 0: # +2 - podminka - pokud je muj soucet vetsi nez 21 a zaroven je jedna ma karta Eso, tak zmensit muj souect o 10
                u_v -= 10
                u_ace -=1
                                
            n = len(u_karty)
            u_karty2 = ""
            for i in range(n):
                u_karty2 += str(u_karty[i]) + " "
                
            n = len(pc_karty)
            pc_karty2 = ""
            for i in range(n):
                pc_karty2 += str(pc_karty[i]) + " "
                
            print "Tve karty - " + str(u_karty2) + "- soucet: " + str(u_v)
            print "Karty pocitace - " +str(pc_karty2) + "- soucet:" + str(pc_v)
            if u_v > 21:
                print "\nPrekrocil jsi v souctu 21"
                sleep(1)
                break
            continue
        elif u in ne:
            break
        else:
            print"Napis prosim ano nebo ne."
            continue
    
    while pc_v < 17:
        pc = b[0]
        pc_karty.append(pc)
        if pc == "J" or pc == "Q" or pc == "K": # vsechny karty vetsi nez 10 maji hodnotu 10
            pc = 10
        if pc == "A": # pocitadlo Es hrace
            pc = 11
            pc_ace += 1
        pc_v += pc
        c.append(b[0])
        del b[0]
        
        if pc_v > 21 and pc_ace > 0: # pokud je muj soucet vetsi nez 21 a zaroven je jedna ma karta Eso, tak pocita Eso jako jednicku
                pc_v -= 10
                pc_ace -=1
    
    n = len(u_karty)
    u_karty2 = ""
    for i in range(n):
        u_karty2 += str(u_karty[i]) + " "
        
    n = len(pc_karty)
    pc_karty2 = ""
    for i in range(n):
        pc_karty2 += str(pc_karty[i]) + " "
                              
    print "Tve karty: " + str(u_karty2) + ", soucet: " + str(u_v)
    print "Karty pocitace: " +str(pc_karty2) + ", soucet:" + str(pc_v)
    print "\n"
    if u_v > 21: # +9 - vypsani vysledku
        print "Prohral jsi"
        pc_p += 1
        vklad -= sazka
    elif pc_v > 21 and u_v <=21:
        print "Vyhral jsi"
        u_p += 1
        vklad += sazka
    elif u_v == pc_v:
        print "Remiza"
    elif u_v > pc_v:
        print "Vyhral jsi"
        vklad += sazka
        u_p += 1
    else:
        print "Prohral jsi"
        pc_p += 1
        vklad -= sazka
        
    c_n = len(c) # +4 - zamichani karet, ktere jsou na stole
    for i in range(c_n):
        x = randrange(0,c_n-i)
        d.append(c[x])
        del c[x]
    
    print "HRAC: " + str(u_p) + " : " + str(pc_p) + " POCITAC"
    if otazka in ano:
        print "Tvuj zustatek: " + str(vklad)
    
    b.extend(d) # vlozeni zamichanych karet ze stolu na spodek hraciho balicku
            
    while True:
        if otazka in ano:
            if vklad == 0:
                prachy = raw_input("Hodnota tveho vkladu je na nule. Chces vlozit dalsi penize? ")
                prachy = prachy.lower()
                if prachy in pomoc:
                    print "\n" + about
                    continue
                if prachy in ano:
                    while True:
                        try:
                            dobit = raw_input("Zadej castku kterou chces dobit: ")
                            dobit = dobit.lower()
                            if dobit in pomoc:
                                print "\n" + about
                                continue
                            dobit = int(dobit)
                            if dobit <= 0:
                                print "Zadej prosim cele cislo vetsi nez 0."
                                continue
                            break
                        except ValueError:
                            print("Zadej prosim cele cislo.")
                            continue
                    
                    print"Dobito!"
                    vklad += dobit
                    sleep(1)
                elif prachy in ne:
                    print"\n"
                    print"=== VYSLEDNE SKORE ==="
                    print "HRAC: " + str(u_p) + " : " + str(pc_p) + " POCITAC"
                    if otazka == "ano":
                        print "Hodnota tveho vkladu: " + str(vklad)
                    otazka = "whatever"
                    print"\n"
                    raw_input("Diky za hru. V pripade nalezeni nejake chyby mi nevahej napsat na lukas.kachtik@fei.com. Pro ukonceni zmackni Enter.")
                    break
                else:
                    print"Napis prosim ano nebo ne."
                    continue
        otazka2 = raw_input("Chces hrat znovu? ")
        otazka2 = otazka2.lower()
        if otazka2 in pomoc:
            print "\n" + about
            continue
        if otazka2 in ano:
            break
        if otazka2 in ne:
            print"\n"
            print"=== VYSLEDNE SKORE ==="
            print "HRAC: " + str(u_p) + " : " + str(pc_p) + " POCITAC"
            if otazka == "ano":
                print "Hodnota tveho vkladu: " + str(vklad)
            otazka = "easteregg"
            print"\n"
            raw_input("Diky za hru. V pripade nalezeni nejake chyby mi nevahej napsat na lukas.kachtik@fei.com. Pro ukonceni zmackni Enter.")
            break
        else:
            print"Napis prosim ano nebo ne."
            continue