global vards, uzvards, vecums, atzime
def varda_parabude(vards): #funkcija pārbauda vai ievadītais vārds ir derīga, vai ir tikai burti
    if not vards.isalpha():
        print('Kļūda: Nedrīkst būt skaitļu!\n')
        return False
    return True
#strip?

def varda_izsakts(vards):
    return vards.strip().capitalize()

def vecuma_parbaude(vecums):
    if not vecums.isdigit(): #pārbauda vai ir saktiļi ne burti
        print('Kļūda: Vecumam jābūt skaitlim\n')
        return False
    if int(vecums) <0:#sakitlimn jābūt pozitīvam
        print('Kļūda: Vecumsam jābūt > 0!\n')
        return False
    return True

def atzimes_parbuade(atzime):
    if not atzime.isdigit():
        print('Kļūda: Atzīmei jābūt skaitlim!\n')
        return False
    if int(atzime) >10:
        print('Kļūda: Atzīme nevar būt >10 !')
        return False
    if int(atzime) <0:
        print('Kļūda: Atzīmei jābut >0!')
        return False
    return True



def ieraksts(faila_nos):#1 funkcija
    try:
        with open(faila_nos, 'a', encoding='utf8') as file:
            while True:
                print('Ievadiet jaunu ierakstu vai ievadiet "stop", lai pātrauktu programmu')
                for i in range(1, 4):
                    vards = input('Ievadiet vārdu: ')
                    if vards == 'stop':
                        print('Jūs izgājāt no programmas. Uzrdzešanos!')
                        break
                    if varda_parabude(vards):
                        vards = varda_izsakts(vards)
                        break

                for i in range(1, 4):
                    uzvards = input('Ievadiet uzvārdu: ')
                    if varda_parabude(uzvards):
                        uzvards = varda_izsakts(uzvards)
                        break

                for i in range(1, 4):
                    vecums = input('Ievadiet vecumu: ')
                    if vecuma_parbaude(vecums):
                        break

                for i in range(1, 4):
                    atzime = input('Ievadiet gala atzīmi (1-10): ')
                    if atzimes_parbuade(atzime):
                        break
                
                turpinat = input('Vai vēlaties ievadīt vēl vienu ierakstu? (ja/ne): ')
                if turpinat == 'ja':
                    ieraksts(faila_nos)
                elif turpinat == 'ne':
                    break
                else:
                    print('Kļūda: Nepareiza ievade!\n')

    except Exception as e:
        print(f"Kļūda sagalbājiet datus failā: {e}")
    #global vards, uzvards, vecums, atzime


def atzime_no_faila(ieraksts):
    #Izvelk atzīmi no datu ieraksta
    try:
        atzime = int(ieraksts.strip().split(",")[-1])
        return atzime
    except (IndexError, ValueError):
        return 0  # Ja formāts nav pareizs, atgriež 0


def sakartot_un_paradit_datus(faila_nos):
    #Sakārto datus pēc vecuma un parāda tos konsolē.
    try:
        with open(faila_nos, "r", encoding="utf-8") as fails:
            dati = fails.readlines()

        if not dati:
            print("Fails ir tukšs. Lūdzu, pievienojiet datus vispirms.")
        else:
            # Kārtošana pēc vecuma
            sakartoti_dati = sorted(dati, key=atzime_no_faila)

            print("\nDati, sakārtoti pēc atzīmes:")
            for ieraksts in sakartoti_dati:
                print(ieraksts.strip())
    except FileNotFoundError:
        print(f"Fails '{faila_nos}' nepastāv. Lūdzu, pievienojiet datus vispirms.")


def datu_pievinosana(vards, uzvards, vecums, atzime, faila_nos): #2
    try:
        with open(faila_nos, 'a', encoding='utf8') as fails:
            #dati tiek saglabāti teksta failā
            fails.write(f"{vards}, {uzvards}, {vecums}, {atzime}\n")
            print('Dati ir pievienoti!')
    except ValueError:
        print('kļūda')
                    

def galvena():
    faila_nos = 'kontroldarbs.txt'

    ieraksts(faila_nos)

    while True:
        print('Izvēlieties darbību: ')
        print('1 - Ievadīt datus')
        print('2 - Saglabāt datus failā')
        print('3 - Parādīt datus sakārtotus datus (augošā secībā)')
        print('4 - Iziet no programmas')

        liet_ievade = input('Jūsu izvēle: ')

        if liet_ievade == '1':
            ieraksts(faila_nos)
        elif liet_ievade == '2':
            print('Šī iespēja šobrīd nav pieejama')
            #datu_pievinosana()
        elif liet_ievade == '3':
            sakartot_un_paradit_datus(faila_nos)
        elif liet_ievade == '4' or 'stop':
            print('Jūs izgājāt no programmas. Uzrdzešanos!')
            break
        else:
            print('Kļūda: Nepareiza ievade!')




galvena()
