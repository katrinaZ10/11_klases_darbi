
import csv
faila_nos = 'pdAtvilde.csv'

def izveidot_failu():
    with open(faila_nos, 'w', newline='', encoding='utf8') as fails:
        writer = csv.writer(fails)
        writer.writerow(['Pilsēta', 'Iedzīvotāju skaits'])
        for i in range(5):
            while True:
                pilseta = input(f"Ievadiet {i+1}. pilsētas nosaukumu: ")
                if pilseta:
                    try:
                        iedzivotaji = int(input(f"Ievadeit {pilseta} iedzīvotāju skaitu: "))
                        writer.writerow([pilseta, iedzivotaji])
                        break
                    except ValueError:
                        print('Kļūda: nepareiza ievade!')
                else:
                    print('Kļūda: nepareiza ievade!')


            
def nolasit():
    try:
        with open(faila_nos, 'r', encoding='utf8') as fails:
            lasitajs = csv.reader(fails)
            next(lasitajs)
            for rinda in lasitajs:
                print(f"Pilsēta : {rinda[0]}, Iedzīvotāju skaits: {rinda[1]}")
                print("-"*12)

    except FileNotFoundError: #ja fails natiek atrasts, tad programma met kļūdu
        print(f"Kļūda: Fails {faila_nos} nav atrasts!")   

def iedz_kopa():
    try:
        with open(faila_nos, 'r', encoding='utf8') as fails:
            lasitajs = csv.reader(fails)
            next(lasitajs)
            kopsumma = sum(int(rinda[1]) for rinda in lasitajs)
        print('-'*12)
        print(f"Iedzīvotāju kopskatis pa pilsētām: {kopsumma}")
        print('-'*12)

    except FileNotFoundError or ValueError as e: #ja fails natiek atrasts, tad programma met kļūdu
        print(f"Kļūda: {e}")   


iedz_kopa()


