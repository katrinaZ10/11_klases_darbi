#tukšs saraksts, kur būs mašīnas
masinas = []

def pievienotMasinu(nosaukums, marka, gads):
    masinas.append({
        'nosaukums':nosaukums,
        'marka':marka,
        'gads':gads
    })
    print(f"Mašīna ' {nosaukums} ' pievienota sarakstam")    

def paraditMasinas():
    if masinas:
        print("\nMašīnas sarakstā: ")
        for masina in masinas:
           print(f"Nosaukums: {masina['nosaukums']}, Marka: {masina['marka']}, Gads: {masina['gads']}")
    else:
        print('\nSaraksts tukšs!')


def atjaunotMasinu(nosaukums, jaunaMarka, jaunsGads):
    for masina in masinas:
        if masina['nosaukums'] == nosaukums:
            masina['marka'] = jaunaMarka
            masina['gads'] = jaunsGads
            print(f"Mašīna '{nosaukums}' atjaunināta.")
            return
    print(f"Mašīna '{nosaukums}' nav atrasta sarakstā.")

def dzestMasinu(nosaukums):
    for masina in masinas:
        if masina['nosaukums'] == nosaukums:
            masinas.remove(masina)
            print(f"Mašīna '{nosaukums}' ir dzēsta no saraksta.")
            return
        print(f"Mašīna '{nosaukums}' nav atrasta sarakstā.")

while True:
    print("\nIzvēlieties darbību!")
    print("1. Pievienot mašīnu\n2. Parādīt visas mašīnas\n3. Atjaunot mašīnu\n4. Dzēst mašīnu\n5. Iziet")
    ievade = input('Ievadiet darbību(1-5): ')
    if ievade == '1':
        nosaukums = input('Mašīnas nosaukums: ')
        marka = input('Ievadiet mašinas marku: ')
        gads = int(input('Ievadiet mašīnas gadu: '))
        pievienotMasinu(nosaukums,marka, gads)
    elif ievade == '2':
        paraditMasinas()
    elif ievade == '3':
        nosaukums = input('Ievadiet nosaukums, kuru vēlaties atjaunot: ')
        jaunaMarka = input('Ievadiet jauno marku: ')
        jaunsGads = int(input('Ievadiet jauno gadu: '))
        atjaunotMasinu(nosaukums, jaunaMarka, jaunsGads)
    elif ievade == '4':
        nosaukums = input('Ievadiet kuru mašīnu vēlaties dzēst: ')
        dzestMasinu(nosaukums)
    elif ievade == '5':
        print('Uzredzēšanos!')
        exit() #break iziet no cikla exit no koda
    else:
        print('Nepareiz ievade! Ievadiet skaitli no 1 līdz 5!')


