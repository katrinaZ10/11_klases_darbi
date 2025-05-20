import csv 
from datetime import datetime

class Rekins:
    def __init__(self, klients, veltijums, izmers, materials): #konstruktors
        self.klients = klients #lauki
        self.veltijums = veltijums
        self.izmers = izmers #platums, garums, augstums
        self.materials = materials

        self.laiks = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.darba_samaksa = 15
        self.PVN = 21
        #self.summa = 0 #aprēķinās vēlāk, izsaucot apreikins()
        self.summa = self.aprekins() #aprēķinās pēc objekta izveidošanas, pamatojoties uz citeim parametriem

    def aprekins(self): #self atsaucas uz pašreizējo objektu(15 rinda), tātad uz visiem atribūtiem, kas objektam ir pieejami
        #'izpakot' izmērus
        platums, garums, augstums = self.izmers
        veltijums_garums = len(self.veltijums)

        produkta_cena = (veltijums_garums * 1.20) + (platums/100) * (garums/100) * (augstums/100)/3*self.materials
        pvn_summa = (produkta_cena + self.darba_samaksa) * self.PVN/100
        reikina_summa = (produkta_cena +self.darba_samaksa) + pvn_summa

        return round(reikina_summa,2)
    
    def izdruka(self):
        print('\n------RĒĶINS------\n')
        print('Klients: ', self.klients)
        print('Veltījums: ', self.veltijums)
        print(f"Izmēri (cm): {self.izmers[0]} x {self.izmers[1]} x {self.izmers[2]}")
        print('Materiāla cena (EUR/cm^3): ', self.materials)
        print('Darba samaksa: ', self.darba_samaksa, 'EUR')
        print('Rēķinaizveidaes laiks: ', self.laiks)
        print('Atmaksas summa: ', self.summa, 'EUR')

    def saglabat(self):
        datnes_nosaukums = f"reikins_{self.klients}_{datetime.now().strftime('%Y-%m-%d')}.csv"
        with open(datnes_nosaukums, 'w', newline='', encoding='utf8') as fails:
            rakstitajs = csv.writer(fails)
            rakstitajs.writerow(['Izveidošanas laiks', 'Klients', 'Veltījums', 'Izmērs', 'Cena (EUR/cm^3)', 'Darba samaksa', 'Summa (EUR)'])
            rakstitajs.writerow([self.laiks, self.klients, self.veltijums,
                                f"{self.izmers[0]} x {self.izmers[1]} x {self.izmers[1]}",
                                self.materials, self.darba_samaksa, self.summa])
            
            print(f"Rēķins saglabāts failā:  {datnes_nosaukums}")

#objektu izsaukšana

print('------Sveiki!------')
klients = input('Klienta vārds: ')
veltijums = input('Veltījums: ')
platums = int(input('Kastītes platums: '))
garums = int(input('Kastītes garums: '))
augstums = int(input('Kastītes augstums: '))
materials = float(input('Materiāla cena: '))

#jauna rēķina objekta izveidošana
reikins = Rekins(klients, veltijums, [platums, garums, augstums], materials)

#saglabāt un izdrukāt rēķinu
reikins.saglabat()
reikins.izdruka()
#reiks.apreikins() #ja pie laukiem liek ka summa=0



