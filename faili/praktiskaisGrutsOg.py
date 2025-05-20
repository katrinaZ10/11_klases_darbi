# ierakstīt teksta failā(no programmas) vārd, uzvārdu un vecumu
'''dot iespēju ievēlēties: 
1- pieveinot datus, 
2 - nolasīt datus 
3 - parādīt sakārtot datus pēc vecuma
4 - iziet
apstrādāt kļūdas( ka nepieņem neparaizu datu veidu)
def pieveinotDatusFailam , def sakartotPecVecuma , def paraditSakartotusDatus
'''
def parbaudit_vardu(vards):
    if not vards.isalpha():
        print('Vārdā drīkst būt tikai burti!')
        return False #secina ka nav pareizi
    return True#isalpha pārbauda vai ir tikai burti

def validet_vecumu(vecums):#pārbauda vai ir sakitļi un vai pozitīvs
    if not vecums.isdigit():
        print('Vecumam jābūt skaitlim!')
        return False
    if int(vecums) <=0:
        print('Ievadiet pozitīvu skaitli!')
        return False
    return True
    
def normalizet_vardu(vards):
    return vards.strip().capitalize()#noņem liekās atstarpes un kapitalizē pirmo burtu

def dublikats(vards, uzvards, vecums, faila_nosaukums):
    try:
        with open(faila_nosaukums, 'r', encoding='utf8') as file:
            dati = file.readlines()
        ieraksts = f"{vards}, {uzvards}, {vecums}\n"
        return ieraksts in dati
    except FileNotFoundError:
        return False #fails nav izveidot, tātad dublikātu nav

def pievienot(faila_nosaukums):
    try:
        with open(faila_nosaukums, 'a', encoding='utf8') as file:
            while True:
                vards = input('Ievadiet vārdu: ')
                if parbaudit_vardu(vards):
                    vards = normalizet_vardu(vards)
                    break

            while True: 
                uzvards = input('Ievadiet uzvārdu: ')
                if parbaudit_vardu(uzvards):
                    uzvards = normalizet_vardu(uzvards)
                    break

            while True:
                vecums = input('Ievadiet vecumu: ')
                if validet_vecumu(vecums):
                    break
            
            if dublikats(vards, uzvards, vecums, faila_nosaukums):
                print('Šis ieraksts jau pastāv!')
                return

            #dati tiek saglabāti teksta failā
            file.write(f"{vards}, {uzvards}, {vecums}\n")
            print('Dati ir pievienoti!')
    except Exception as e:
        print(f"Kļūda sagalbājiet datus failā: {e}")


def paradit_datus(faila_nosaukums):
    try:
        with open(faila_nosaukums, 'r', encoding='utf8') as file:
            dati = file.readlines()
        if not dati: #pārbauda vai failā ir dati
                print('Fails ir tukšs. Pievienojiet datus.')
        else:
            print('\nDati no faila: ')
            for ieraksts in dati:
                print(ieraksts.strip())
    except FileNotFoundError:
        print(f"Fails {faila_nosaukums} nepastāv! ")

def iegut_vecumu_no_datiem(ieraksts):
    try:
        vecums = int(ieraksts.strip().split(",")[-1])
        return vecums
        #ja formāts nav pareizs atrgriežs 0
    except (IndexError, ValueError):
        return 0

def sakartot(faila_nosaukums):
    try:
        with open(faila_nosaukums, 'r', encoding='utf8') as file:
            dati = file.readlines()
        if not dati: #pārbauda vai failā ir dati
            print('Fails ir tukšs. Pievienojiet datus.')
        else:
            #kārtošana
            sakartot_dati = sorted(dati, key = iegut_vecumu_no_datiem)
            print('\nPēc vecuma sakārtoti dati:')
            for ieraksts in sakartot_dati:
                print(ieraksts)
    except FileNotFoundError:
        print(f"Fails {faila_nosaukums} nepastāv! ")    

#programmas galvenā daļa
def izvele():
    faila_nosaukums = 'dati.txt'

    while True:

        print('\nIzvēlēties opciju: ')
        print('1 - Pieveinot datus')
        print('2 - Parādīt datus')
        print('3 - Parādīt sakārtotus datus pēc vecuma')
        print('4 - iziet')

        izvele = input('Izvēle: ')

        if izvele == '1':
            pievienot(faila_nosaukums)
        elif izvele == '2': #nolasa datus no faila ar for ciklu
            paradit_datus(faila_nosaukums)
        elif izvele == '3':
            sakartot(faila_nosaukums)
        elif izvele == '4':
            print('Izvēle tiek pārtarakta! ')
            break
        else:
            print('Nepareiza datu ievade! Mēģināt vēlreiz!')

    
izvele()    

   

