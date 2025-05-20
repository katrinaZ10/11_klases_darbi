
class Kubs(): #Bāzes klases izveide

    def __init__(self,  krasa, malas_garums): #konstruktors
        #malas garums var būt 2-10
        if malas_garums>=2 and malas_garums<=10:
            self.malas_garums = malas_garums
        else: 
            print('Malas garums neatbilst nosacījumiem!')
            self.malas_garums = 2 #malas garumam neatbilstot nosacījumiem, tik iestatīts kā 2
        self.krasa = krasa
    
    def aprekinat_tilpumu(self): #metode atgriež kuba tilpumu
        tilpums = self.malas_garums**3
        return tilpums


class Bloks(Kubs):

    def __init__(self, skaits, krasa, malas_garums, forma):
        super().__init__(krasa,malas_garums)
        if skaits>=1 and skaits<=4:
            self.skaits = skaits
        else:
            print('Nepareiza kubu sakita vērtība!')
            self.skaits = 1
        
        self.nosaukums = str(self.krasa)+str(self.skaits)

        formas_vertibas = [11, 12, 13, 14, 22]
        if forma not in formas_vertibas:
            print('Forma neatbilst nosacījumiem!')
            self.derigums = 'nederīgs 0'
        else:
            self.derigums = 'derīgs 1'

    def tilpums(self):
        kuba_tilpums = self.malas_garums**3
        bloka_tilpums = kuba_tilpums * self.skaits
        return bloka_tilpums

    def mainit_formu(self, jauna_forma):
        formas_vertibas = [11, 12, 13, 14, 22]
        if jauna_forma not in formas_vertibas:
            print('Forma neatbilst nosacījumiem!')
            self.derigums = 'nederīgs 0'
        else:
            self.derigums = 'derīgs 1'

#objekta izveide
print('Dati par kubg objektu:')
kubg = Kubs('Zaļš',10)
print('Kubg krāsa un tilpums: ',kubg.krasa, kubg.aprekinat_tilpumu())
print('Kubg malas garums: ', kubg.malas_garums)
print('***')

print('Dati par kubr objektu:')
kubr = Kubs('Sarkans', 1)
print('Kubr krāsa un tilpums: ',kubr.krasa , kubr.aprekinat_tilpumu())
print('Kubr malas garums: ', kubr.malas_garums)
print('***')

print('Oranžs objekts: ')
orange3 = Bloks(3, 'oranža', 5, 13)
print(orange3.nosaukums, orange3.tilpums(), orange3.derigums)
print('***')

print('Zilasi objekts: ')
blue5 = Bloks(5 ,'zila', 7, 23)
print(blue5.nosaukums, blue5.tilpums(), blue5.derigums)

print('Mainīta forma: ')
blue5.mainit_formu(12)
print(blue5.nosaukums, blue5.tilpums(), blue5.derigums)


