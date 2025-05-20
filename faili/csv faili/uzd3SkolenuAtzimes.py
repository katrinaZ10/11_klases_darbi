#uzd3 - jaunā failā
#no faila skoleni.csv noteikt, kurš skolēns ieguvis, visaugstāko vidējo vērtējumu
#vidējo vērtējumu, parādīt skolēna vārdu un vērtējumu


import csv

faila_nosaukums = 'skoleni_videjais.csv'


with open(faila_nosaukums, 'r', encoding='utf8') as file:#mainīgais 'file' attēlo atvērto failu
    #nolasa csv failu un katru rindu pārveido par vārdnīcu(kolonna:atslēga, vērtība:ieraksts)
    reader = csv.DictReader(file)
    skoleni = list(reader) #pārveido vārdnīcu par list, lai vieglāk darboties
    #katrs saraksta elements ir 1 ieraksts no csv faila

#rēķina vidējo un pievieno jaunu laiku
for skolens in skoleni:
    matematika = int(skolens['Matemātika'])
    ang_val = int(skolens['Angļu valoda'])
    sports = int(skolens['Sports'])

    videjais = round((matematika+ang_val+sports)/3, 2)#,2 ir 2 cipari aiz ,
    #katram skolaēnam ieraksts tiak pārveidots 
    skolens['Vidējais'] = videjais
    field_names = skoleni[0].keys()
    
for skoleens in sorted(skolens):
    print(skoleens)
#kartots = sorted(skoleni[4])
#print(kartots)
    

