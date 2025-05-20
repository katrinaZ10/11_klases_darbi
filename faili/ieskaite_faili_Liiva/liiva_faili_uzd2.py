
import csv
faila_nosaukums = 'Liiva_dati.csv'

pilsetas = [
    {'Nosaukums': 'Sigulda',
    'Iedzīvotāji': 2999},
    {'Nosaukums': 'Loja',
    'Iedzīvotāji': 12},
    {'Nosaukums': 'Liepāja',
    'Iedzīvotāji': 5462},
    {'Nosaukums': 'Aizpute',
    'Iedzīvotāji': 3876},
    {'Nosaukums': 'Cēsis',
    'Iedzīvotāji': 587},

]

def ieraksta_izveide():
    with open(faila_nosaukums, 'w', newline='', encoding='utf8') as fails:
        nosaukumi = ['Nosaukums', 'Iedzīvotāji'] #kolonnu nosaukumi
        rakstitajs = csv.DictWriter(fails, nosaukumi)
        rakstitajs.writeheader()
        rakstitajs.writerows(pilsetas)
    print(f"Dati saglabāti {faila_nosaukums}. ")

def liet_izveido(): #funkcija met kļūdas!!!!
    try:
        with open(faila_nosaukums, 'w', newline='', encoding='utf8') as fails:
            nosaukumi = ['Nosaukums', 'Iedzīvotāji'] #kolonnu nosaukumi
            rakstitajs = csv.DictWriter(fails, nosaukumi)
            rakstitajs.writeheader()

            for i in range(1,6):
                nosaukums = input(f"Pilsētas {i}. nosaukums: ")
                iedz_sk = input(f"Pilsētas {nosaukums} iedzīvotāju skaits: ")
                rakstitajs.writerows([nosaukums, iedz_sk])
        print('Dati ir pieveinoti!')
    except FileNotFoundError:
        print('Kļūda: fails neeskistē!')


def paradit_pilsetas(): #funkcija uz konsoles izdrukā failā saglabāto informāciju
    try:
        with open(faila_nosaukums, 'r', encoding='utf8') as fails:
            lasitajs = csv.DictReader(fails) #mainīgajā "lasītājs" ir saglabāta faila informācija lai vieglāk būtu programmējot piekķlūt
            for rinda in lasitajs:
                print(f"Nosaukums: {rinda['Nosaukums']}, Iedzīvotāju skaits: {rinda['Iedzīvotāji']}. ")
                print('-'*20)

    except FileNotFoundError:
        print(f"Kļūda: '{faila_nosaukums}' netika atrasts!")
        
def iedzivotaju_aprekini():
    #sakuma_summa = 0
    with open(faila_nosaukums, 'r', encoding='utf8') as fails:
        lasitajs = csv.DictReader(fails)
        saturs = list(lasitajs)
        for rinda in saturs:
            skaits = int(rinda['Iedzīvotāji'])
            kopsumma = (kopsumma+skaits)
            #for i in skaits:
             #   kopsumma = kopsumma+i
        print('kopsumma: ', kopsumma)




#ieraksta_izveide()
#paradit_pilsetas()
#iedzivotaju_aprekini()
#liet_izveido()


