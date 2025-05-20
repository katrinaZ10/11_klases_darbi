
def parbaudaAtzimi(ievade):
    #pārbaude
    if ievade in range(0, 101): #ar range funkciju pārbaude atzīmes
        if ievade in range(0, 11):
            print('Rezultāts: ', ievade, '% - Ļoti slikti (Atzīme: 1)')
            vertejums = 'Ļoti slikti'
            atzime = 1
        elif ievade in range(11, 21):
            print('Rezultāts: ', ievade, '% - Slikti (Atzīme: 2)')
            atzime = 2
            vertejums = 'Slikti'
        elif ievade in range(21, 31):
            print('Rezultāts: ', ievade, '% - Vāji (Atzīme: 3)')
            atzime = 3
            vertejums = 'Vāji'
        elif ievade in range(31, 41):
            print('Rezultāts: ', ievade, '% - Knapi (Atzīme: 4)')
            atzime = 4
            vertejums = 'Knapi'
        elif ievade in range(41, 54):
            print('Rezultāts: ', ievade, '% - Viduvēji (Atzīme: 5)')
            atzime = 5
            vertejums = 'Viduvēji'
        elif ievade in range(54, 67):
            print('Rezultāts: ', ievade, '% - norm (Atzīme: 6)')
            atzime = 6
            vertejums = 'norm'
        elif ievade in range(67, 76):
            print('Rezultāts: ', ievade, '% - Gandrīz labi (Atzīme: 7)')
            atzime = 7
            vertejums = 'Gandr;iz labi'
        elif ievade in range(76, 87):
            print('Rezultāts: ', ievade, '% - Labi (Atzīme: 8)')
            atzime = 8
            vertejums = 'Labi'
        elif ievade in range(87, 95):
            print('Rezultāts: ', ievade, '% - Ļoti labi (Atzīme: 9)')
            atzime = 9
            vertejums = 'Ļoti labi'
        elif ievade in range(95, 101):
            print('Rezultāts: ', ievade, '% - Izcili (Atzīme: 10)')
            atzime = 10
            vertejums = 'Izcili'
    else:
        print('Nepareiza ievade! Lūdzu ievadeit skaitli no 0 - 100.')
    return atzime, vertejums

def ievaditRezultatu():
    while True:
        try:
            ievade=float(input('Testa rezultāts (0-100)'))
            if ievade >=0 and ievade<=100:
                return ievade
            else:
                print('Ievadiet rezultātu no 0-100')
        except ValueError:
            print('Nederīga datu ievade!')

def darbiba():
    while True:
        rezultats = ievaditRezultatu()
        vertejums, atzime = parbaudaAtzimi(rezultats)
        print(f"Rezultāts: {rezultats}% - {vertejums} (atzīme {atzime})\n")

        turpinat= input('Vai jūs vēlaties beigt(ja/ne): ')
        if turpinat!= 'ja':
            print('Programma beigusies!')
            break



darbiba()