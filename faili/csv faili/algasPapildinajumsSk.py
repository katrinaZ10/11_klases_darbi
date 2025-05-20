#izveiedot jaunu failu, cour programmu un nolasīt konkrētās rindas
#ievietot failā 5 ierkastus, parādu tos kuriem >1000
import csv 

csv_fails = 'darbinieki.csv'
#ierakstītāmie dati

'''def algas_parbaude(alga):

    if alga.isdigit() and int(alga)>0:
        return True
    else:
        print("Kļūda: Alga ir nederīga! ")
        return False'''


darbinieku_saraksts = [
    {'Vārds': 'Anna', 
    'Amats':'Skursteņslauķis', 
    'Alga':'850'},
    {'Vārds': 'Romčiks', 
    'Amats':'Virsleitnants', 
    'Alga':1500},
    {'Vārds': 'Laura', 
    'Amats':'Supermodele', 
    'Alga':'b'},
    {'Vārds': 'Tommijs', 
    'Amats':'Vidospēļu tetētāja', 
    'Alga':800},
    {'Vārds': 'Lora', 
    'Amats':'Supervaronis', 
    'Alga':194793},

]

try:
    with open(csv_fails, 'w', encoding='utf8', newline='') as fails:
        field_names = ['Vārds', 'Amats', 'Alga'] #kolonnu nosaukumi
        writer = csv.DictWriter(fails, field_names)
        writer.writeheader() #kolonnu virsraksti
        writer.writerows(darbinieku_saraksts)

    with open(csv_fails, 'r', encoding='utf8') as fails:
        reader = csv.DictReader(fails)
        algas_filtrs = []
        for rinda in reader:
            try:
                alga = int(rinda['Alga'])
                if alga > 1000:
                    algas_filtrs.append(rinda)
            except ValueError:
                print(f"Brīdinājums: Rinda {rinda['Vārds']} {rinda['Amats']} nav derīga alga!")
        if algas_filtrs:
            for darbinieks in algas_filtrs: #pd būs FOR cikli
                 print(f"Vārds: {darbinieks['Vārds']}, Amats: {darbinieks['Amats']}, Alga: {darbinieks['Alga']}")
        else:
            print('Nav tādu darbinieku!')
except FileNotFoundError:
    print(f"Fails '{csv_fails}' nav atrasts!")
except Exception as e:
    print(f"Kļūda nolasot failu: {e}")


#datu ierakstīšana failā
'''try: 
    with open(csv_fails, 'w', encoding='utf8', newline='') as fails:
        field_names = ['Vārds', 'Amats', 'Alga'] #kolonnu nosaukumi
        writer = csv.DictWriter(fails, field_names)
        writer.writeheader() #kolonnu virsraksti
        writer.writerows(darbinieki)

    #nolasīt failu saturu un parādīt kuriem alga >1000
    with open(csv_fails, 'r', encoding='utf8') as fails:
        reader = csv.DictReader(fails)
        for rinda in reader:
            alga = rinda['Alga']
            algas_parbaude(alga)
        
        #for rinda in reader:
        #   if int(rinda['Alga'])>1000:
        #      print(f"Vārds: {rinda['Vārds']}, Amats: {rinda['Amats']}, Alga: {rinda['Alga']}")
except FileExistsError:
    print(f"Kļūda: Fails {csv_fails} neeksistē!")'''



#jāpārbauda vai alga ir derīgs skaitlis
#ja nav derīgs skaitlis, tad izdrukāt brīdinājumu
#ja fails darbinieki.csv neekistē, tad izdrukāt kļūdas pziņojumu


#uzd3 - jaunā failā
#no faila skoleni.csv noteikt, kurš skolēns ieguvis, visaugstāko vērtējumu
#vidējo vērtējumu, parādīt skolēna vārdu un vērtējumu

