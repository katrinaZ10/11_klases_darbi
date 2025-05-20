'''def ievades_parbaude(veids, positive):
    try:
        ievade = input(veids, positive)
        if positive <= 0:
            print('Jābūt pozitīvam sakitlim!')
        else:
            ()
    except ValueError:
        print('Nepareizs ievadītais datu tips!')
    
    return ievade'''

cels_kopa = 0
cena_kopa = 0
laiks_kopa = 0
pieturu_nosaukumi = []

def vilciena_aprekini():
    attalums = float(input('Ievadiet attālumu līdz pieturai (km): '))
    biletes_cena = float(input('Ievadiet vilciena biļetes cenu (EUR): '))
    laiks = float(input('Ievadiet cik ilgi būs jābrauc (h): '))
    cels_kopa =+attalums
    cena_kopa =+ biletes_cena
    laiks_kopa =+ laiks
    return cels_kopa, cena_kopa, laiks_kopa

def autobusa_aprekini():
    attalums = float(input('Ievadiet attālumu līdz pieturai (km): '))
    biletes_cena = float(input('Ievadiet autobusa biļetes cenu (EUR): '))
    laiks = float(input('Ievadiet cik ilgi būs jābrauc (h): '))
    cels_kopa =+ attalums
    cena_kopa =+ biletes_cena
    laiks_kopa =+ laiks
    return cels_kopa, cena_kopa, laiks_kopa

def staigasanas_apreikini():
    attalums = float(input('Ievadiet attālumu līdz pieturai (km): '))
    laiks = attalums / 5 #cilvēks var noiet 1h = 5km
    biletes_cena = 0 #staigāšana ir par brīvu
    cels_kopa =+ attalums
    cena_kopa =+ biletes_cena
    laiks_kopa =+ laiks
    return cels_kopa, cena_kopa, laiks_kopa

#pieturu_sk=0
def pieturas(skaits):
    for pieturas in range(1, skaits+1):
        pieturas_nos = input(f"Ievadiet {pieturas}.pieturas nosaukumu: ").capitalize() #capitalaze pārvaidos ka pirmasi burts ir lielais
        pieturu_nosaukumi.append(pieturas_nos)
    print('Jūsu maršruts: ', pieturu_nosaukumi) 
    return pieturu_nosaukumi
    


def galvena():
    
    print('Laipni lūgti ekskursijas maršruta plānotājā!')
    print('Komatu vietā liec punktus!')

    while True:
        try:
            skolenu_sk = int(input('\nIevadiet cik skolēni brauks (piemēram: 12): '))
            pieturu_sk = int(input("Ievadiet cik pieturas būs jūsu ekskursijā (visamaz 2 jābūt): ")) 

            for pieturas in range(1, pieturu_sk+1): #ar range funkciju izies cauri katrai pieturai lai zinātu kā lietotājs tur tiks
                pieturas_nos = input(f"Ievadiet {pieturas}.pieturas nosaukumu: ").capitalize() #capitalaze pārvaidos ka pirmasi burts ir lielais
                print('\nIespējamie pārvietošanās veidi: \n> Autobuss\n> Vilciens\n> Kājām')
                parvietosies_ar = input(f"Ievadiet kā jūs tiksiet līdz {pieturas_nos} (bez garumzīmēm): " ).lower()
                if parvietosies_ar == 'autobuss':
                    autobusa_aprekini()
                elif parvietosies_ar == 'vilciens':
                    vilciena_aprekini()
                elif parvietosies_ar == 'kajam':
                    staigasanas_apreikini()
                else:
                    print('Nepareiza datu ievade!')
                    break
                pieturu_nosaukumi.append(pieturas_nos)
                    
            print('Jūsu maršruts: ', pieturu_nosaukumi)        
            print(f"Brauks {skolenu_sk} skolēni")
            print(f"\nKopā vienam skolēnam jāmaksā: {cena_kopa} \nKopā ceļā tiks pavadītas {laiks_kopa} stundas \nKopā ir mēroti {cels_kopa} kilometri")#nestrāda
            beigt = input('Vai vēlateis beigt (ja/ne): ')
            if beigt == 'ja':
                print('Uztikšanos, un drošu ceļu ekskursijā!')
                exit()
            else:
                ()
        except ValueError:
            print('Nepareiza datu ievade!')


galvena()

