# pievienot skaitļus sarkstāam
def pieveinotSkaitli():
    skaitli=[]
    while True: 
        try:
            skaitlis=(int(input('Ievadiet skaitli(0, ja vēlaties beigrt darbu)')))
            if skaitlis == 0:
                break
            skaitli.append(skaitlis)
        except ValueError:
            print('Nepraiza ievade!')
            
    print('Saraksts: ', skaitli)

pieveinotSkaitli()
