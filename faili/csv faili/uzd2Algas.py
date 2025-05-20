#izveiedot jaunu failu, cour programmu un nolasīt konkrētās rindas
#ievietot failā 5 ierkastus, parādu tos kuriem >1000
import csv 

csv_fails = 'darbinieki.csv'
#ierakstītāmie dati

darbinieki = [
    {'Vārds': 'Anna', 
    'Amats':'Skursteņslauķis', 
    'Alga':900},
    {'Vārds': 'Romčiks', 
    'Amats':'Virsleitnants', 
    'Alga':1500},
    {'Vārds': 'Laura', 
    'Amats':'Supermodele', 
    'Alga':350},
    {'Vārds': 'Tommijs', 
    'Amats':'Vidospēļu tetētāja', 
    'Alga':800},
    {'Vārds': 'Lora', 
    'Amats':'Supervaronis', 
    'Alga':194793},

]

#datu ierakstīšana failā
with open(csv_fails, 'w', encoding='utf8', newline='') as fails:
    field_names = ['Vārds', 'Amats', 'Alga'] #kolonnu nosaukumi
    writer = csv.DictWriter(fails, field_names)
    writer.writeheader() #kolonnu virsraksti
    writer.writerows(darbinieki)

#nolasīt failu saturu un parādīt kuriem alga >1000
with open(csv_fails, 'r', encoding='utf8') as fails:
    reader = csv.DictReader(fails)

    for rinda in reader:
        if int(rinda['Alga'])>1000:
            print(f"Vārds: {rinda['Vārds']}, Amats: {rinda['Amats']}, Alga: {rinda['Alga']}")



