#uzd1- ierakstīt .txt failā ar input metodi, failu izveido programma

faila_nosaukums = 'uzdevums_viens.txt'


def ierasktit():
    with open(faila_nosaukums, 'w', encoding='utf8') as fails:
        for i in range(1,7):
            vards = input(f"Ievadiet {i}. vārdu: ")
            fails.write(vards+'\n')
        print('Informācija saglabāta!')
#konkrēti 6 ierakstus

'''def ieraksti_faila():
    dati = input('Raksti te: ')
    with open(faila_nosaukums, 'w', encoding='utf8') as fails:
        fails.write(dati)
    print('Informācija saglabāta!')

ieraksti_faila()

#uzd2 - nolasīt tekstu no faila, Ja nav atrasts fails - infotmāt lietotāju
def nolasit_failu():
    try:
        with open(faila_nosaukums, 'r', encoding='utf8') as fails:
            saturs = fails.read()
            print('\nFaila saturs: ')
            print(saturs)
    except FileNotFoundError: #atceries izmantot File no faound error
        print('Fails netika atrasts!')'''

#ierasktit()

def nolasit_ar_for():
    try:
        with open(faila_nosaukums, 'r', encoding='utf8') as fails:
            print('Faila saturs: ')
            for i in fails:#neņemot liekās atstarpes print(i)
                print(i.strip())
    except FileNotFoundError:
        print('Kļūda: fails nav atrasts!')

#izveidot sarakstu ar 3 vārdein un pieveinot šo sarakstu failā
#un parādīt konsolē cik vārsi pieveinoti

def saraksta_pieveinosana():
    try:
        with open(faila_nosaukums, 'a', encoding='utf8') as fails:
            saraksts = []
            for i in range(1,4):
                ievade = input(f"{i}. saraksta elments: ")
                saraksts.append(i)
                fails.write(ievade+'\n')

    except FileNotFoundError:
        print('Kļūda: Fails nav atrasts!')

def vardi_manuali():#ieskaitē būs
    jauni_vardi = ['Cālis', 'Vista', 'Kaķis']
    try:
        with open(faila_nosaukums, 'a', encoding='utf8') as fails:
            for i in jauni_vardi:
                fails.write(i+'\n')
            print(f"{len(jauni_vardi)} jauni vārdi pieveinoti.") #len() pasaka cik vārdi ir sarakstā
    except FileNotFoundError:
        print('Kļūda: Fails nav atrasts!')

#ievadīt vārdu, ko meklēt un informāet lietpotāju vai tāds ir
def atrast_vardu():
    liet_ievade = input('Kādu vārdu jūs meklējat: ')
    try:
        with open(faila_nosaukums, 'r', encoding='utf8') as fails:
            saturs = fails.read()
        if liet_ievade in saturs:
            print(f"Vārds {liet_ievade} ir atrasts.")
        elif liet_ievade not in saturs:
            print(f"Vārds {liet_ievade} nav atrasts.")
    except FileNotFoundError:
        print('Kļūda: Fails nav atrasts!')

#sakārtot failā esošos datos dilstošā secībā
def sakartot_failu():
    with open(faila_nosaukums, 'r', encoding='utf8') as fails:
        saturs = fails.read()
        for i in range(1, 10):
            print(saturs[-i])
        
def kartot():
    try:
        with open(faila_nosaukums, 'r', encoding='utf8') as fails:
            saturs = fails.readlines()
        kartots = sorted(saturs, reverse=True)
        #iearskta atpakaļ fails
        with open(faila_nosaukums, 'w', encoding='utf8') as fails:
            fails.writelines(kartots)
            print('Fails sakārtot s dilstoš a secībā')
    except FileNotFoundError:
        print('Kļūda: Fails nav atrasts!')

kartot()