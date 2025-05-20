#nolasīt csv failu
#aprēķināt vidēju vērtējumu
#pieveinot jaunu lauku vidējais, to visu saglabā jaunā csv failā
import csv

ievades_fails = 'skoleni.csv'
izvades_dati = 'skoleni_videjais.csv'

with open(ievades_fails, 'r', encoding='utf8') as file:#mainīgais 'file' attēlo atvērto failu
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


#saglabā datus jaunā faila
with open(izvades_dati, 'w', encoding='utf8', newline='')as file:
    field_names = skoleni[0].keys() #atgriežs pirmās kolonnas atslēgas nosaukumu
    #ojekta, kas raksta datus uz csv failu
    writer = csv.DictWriter(file, field_names)#rakstīs pareizā secībā
    #ieraksts pirmo rindu, kas ir kolonnu nosaukumi
    writer.writeheader()
    writer.writerows(skoleni) #iziet cauri sarkastam un katru 

print(f"Jaunais fails ir saglabāts veiksmīgi {izvades_dati}!")



