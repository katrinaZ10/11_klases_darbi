#funkcija izveido csv failu un ieraksts 3 rindas

import csv
faila_nosaukums = 'dati.csv'
def izveidot_csv():
    
    with open(faila_nosaukums, 'w',newline='', encoding='utf8')  as fails:
        rakstitajs = csv.writer(fails)
        rakstitajs.writerow(['ID', 'Vārds', 'Vecums'])
        rakstitajs.writerows([[1, 'Alise', 25], [2, 'Laura', 17] , [3, 'Bella', 84]])
    print('Fails izveidots!')

#izveidot_csv()

#parādīt csv faila saturu

def faila_saturs():
    try:
        with open(faila_nosaukums, 'r', encoding='utf8')  as fails:
            lasitajs = csv.reader(fails)
            for i in lasitajs:
                print(*i)#zvaigznīte * parada smuku konsolei
    except FileNotFoundError:
        print('Kļūda: fails neeskistē!')

#pieveinot jaunu ID, vārdu, vecumu ar input

def pieveinot_jaunu():
    try:

        with open(faila_nosaukums, 'a',newline='', encoding='utf8') as fails:
            rakstitajs = csv.writer(fails)
            Id = input('ID: ')
            vards = input('Vārds: ')
            vecums = input('Vecums: ')
            rakstitajs.writerow([Id, vards, vecums])
        print('Dati ir pieveinoti!')
    except FileNotFoundError:
        print('Kļūda: fails neeskistē!')


pieveinot_jaunu()
faila_saturs()