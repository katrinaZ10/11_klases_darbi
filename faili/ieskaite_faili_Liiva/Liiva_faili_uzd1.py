
faila_nosaukums = 'Liiva_dati.txt'

def izveide_ierakstisana(): #funkcija uzveidos un ierakstīs iezveidotaja failā 10 lietotāja ievadītas pilsētas
    with open(faila_nosaukums, 'w', encoding='utf8') as fails:
        for i in range(1, 11): #ar 'for i in range' funkciju prasīsi lietotājam ievadīt vajadzīgās 10 pilsētas
            pilseta = input(f"Ievadeit {i}. pilsētu: ")
            fails.write(pilseta + '\n')
        print('Faili veiksmīgi pievienoti!')

def nolasisana(): #funkcija nolasiīs jau no izveidota faila informāciju, un ja fails neitiek atrasts, tad met konsolē lietotājam kļūdu
    try:
        with open(faila_nosaukums, 'r', encoding='utf8') as fails:
            #saturs = fails.readlines() #izmantos kā faila "lasītāju"
            print(f"\n'{faila_nosaukums}' fails saturs: ")

            for rindas in fails:
                print(rindas.strip()) #strip noņem liekās atrsatrpes
            
            print('-'*17)
    except FileNotFoundError: #ja fails natiek atrasts, tad programma met kļūdu
        print(f"Kļūda: Fails {faila_nosaukums} nav atrasts!")

def kartots(): 
    try:
        with open(faila_nosaukums, 'r', encoding='utf8') as fails:
            saturs = fails.readlines() #mainīgais saglabā sevī nolasīto informāciju no faila kā list
        kartotas_rindas = sorted(saturs)
        #print(kartotas_rindas)
        for i in kartotas_rindas:
            print(i.strip())

    except FileNotFoundError: #ja fails natiek atrasts, tad programma met kļūdu
        print(f"Kļūda: Fails {faila_nosaukums} nav atrasts!")

def pievienot_jaunu():
    liet_pilsetas = []
    with open(faila_nosaukums, 'a', encoding='utf8') as fails:
        #lasitajs = fails.readlines()
        for i in range(1, 4):
            jaunas_pilsetas = input(f"Ievadiet {i} pilsētu kuru vēlaties pievienot: ")
            if jaunas_pilsetas in liet_pilsetas:
                print(f"{jaunas_pilsetas} ir jau. Mēģini vēlreiz!")
                kluda = input('Ievadi citu pilsētu: ')
                liet_pilsetas.append(kluda)
            else:
                pass
            liet_pilsetas.append(jaunas_pilsetas)
            for i in liet_pilsetas:
                fails.writelines(i+'\n')

    print(f"Tika pieveinotas {len(liet_pilsetas)} : {liet_pilsetas}")

#izveide_ierakstisana()
#kartots()
#pievienot_jaunu()
