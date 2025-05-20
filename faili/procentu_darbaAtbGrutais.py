def parbaude_varda(teksts):
    return teksts.isalpha() and teksts.strip() #pārbauda vai ir tiaki burti

def parbaude_vecums(vecums):
    return vecums.isdigit() and int(vecums)>0#vecuma ierobežojums: vesels un tikai skaitlis

def parbaude_atzime(atzime):
    return atzime.isdigit() and 0<=int(atzime)<10 #atzīmes ierobežojums

def ierobezo_meginajums(parbaudit_def, ievades_teksts, kludas_teksts):
    #ievade ar pārbaudi, kur atļauj max 3 mēģinājumus
    for i in range(3):
        dati = input(ievades_teksts)
        if parbaudit_def(dati):
            return dati
        print(kludas_teksts)
    print('Pārsneigts mēģinājumum skaits!')
    

def iegut_ierakstu():
    ieraksti = []
    while True:
        vards = ierobezo_meginajums(parbaude_varda, 
        'Ievadiet vārdu: ',
        'Kļūda: Vārdā var būt tikai burti')
        if not vards:
            break

        uzvards = ierobezo_meginajums(parbaude_varda, 
        'Ievadiet uzvārdu: ',
        'Kļūda: Vārdā var būt tikai burti')
        if not uzvards:
            break

        vecums = ierobezo_meginajums(parbaude_vecums, 
        'Ievadiet vecumu: ',
        'Kļūda: Vecums var būt tikai cipari un > 0')
        if not vecums:
            break

        atzime = ierobezo_meginajums(parbaude_atzime, 
        'Ievadiet atzīmi: ',
        'Kļūda: Atzīmei var būt tikai cipari un  < 10')
        if not atzime:
            break

        ieraksti.append((vards, uzvards, int(vecums), int(atzime)))

        turpinat = input('Vai turpināt? (ja/ne): ').lower()
        if turpinat != 'ja': #ja nav vināds ar jā, == viendāds, != Nav vienāds
            break
    return ieraksti        

def saglabat_faila(ieraksti, faila_nosaukums = 'kontroldarbsSkVersija.txt'):
    #saglabāt ierakstus ar tabulatoriem ( \t ) starp laukiem
    with open (faila_nosaukums, 'a', encoding='utf8') as fails:
        for ieraksts in ieraksti:
            fails.write('\t'.join(map(str, ieraksts))+'\n') #tagad būs smuks ieraksts
    print(f"Dati saglabāti failā: {faila_nosaukums}")
    

def sakartoti_dati(ieraksti): #parādīs sakaŗtotus datus faiā
    #sakārtoti dati pēc gala atzīmes
    #definē anonīmo funkciju lambda, kas pieņem 1 argumentu x(katrs ieraksts no saraksta)
    kartots = sorted(ieraksti, key=lambda x:x[3])
    print('\nVārds\tUzvārds\tVecums\tAtzīme')
    for ieraksts in kartots:
        print('\t'.join(map(str, ieraksts)))

#def iegut_gala_atzimi(ieraksts):
    #return ieraksts[3]

#kārtošanas opcija ar atsevišķu funkciju
'''def iegut_gala_atzimi(ieraksts):
    return ieraksts[3]
    kartots = sorted(ieraksti, key=i])#key=lamba x:x[3]
    print('\nVārds\tUzvārds\tVecums\tAtzīme')
    for ieraksts in kartots:
        print('\t'.join(map(str, ieraksts)))'''

def izvelne():#programmas galvenā daļa
    ieraksti = []

    while True:
        print('\nIzvēlieties darbību: ')
        print('1 - Ievadīt datus')
        print('2 - Saglabāt datus failā')
        print('3 - Parādīt datus sakārtotus datus (augošā secībā)')
        print('4 - Iziet no programmas')
        izvele = input('Jūsu izvēle: ')

        if izvele == '1':
            ieraksti +=iegut_ierakstu()
        elif izvele == '2':
            if ieraksti:
                saglabat_faila(ieraksti)
            else:
                print('Nav datu, ko saglabāt!')
        elif izvele == '3':
            if ieraksti:
                sakartoti_dati(ieraksti)
            else:
                print('Nav datu, ko parādīt!')
        elif izvele == '4':
            print('Programma tiek pārtraukta.')
            break
        else:
            print('Neapreiza ievade, lūdzu mēģiniet vēlreiz!')

    

izvelne()
#ko darījām: 1. saraksta visas def, ar pass, velāk izdarīs
#2. izveido galveno funkciju/daļu (izvelne)
#3. saraksta ievades pārbaudes (pd būs)
#4. ievades funkcija