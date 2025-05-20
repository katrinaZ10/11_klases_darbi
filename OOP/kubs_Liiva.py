
class Kubs(): #Bāzes klases izveide

    def __init__(self,  krasa, malas_garums): #konstroktors
        #malas garums var būt 2-10
        if malas_garums>=2 and malas_garums<=10:
            self.malas_garums = malas_garums
        else: 
            print('Malas garums neatbilst nosacījumiem!')
            self.malas_garums = 2 #malas garumam neatbilstot nosacījumiem, tik iestatīts kā 2

        self.krasa = krasa
    
    def aprekinat_tilpumu(self): #metode atgriež kuba tilpumu
        return f"{round(self.malas_garums*self.malas_garums*self.malas_garums)}"

#objekta izveide
print('Dati par kubg objektu:')
kubg = Kubs('Zaļš',10)
print('Kubg krāsa un tilpums: ',kubg.malas_garums , kubg.aprekinat_tilpumu())
print('Kubg malas garums: ', kubg.malas_garums)
print('***')

print('Dati par kubr objektu:')
kubr = Kubs('Sarkans', 1)
print('Kubr krāsa un tilpums: ',kubr.krasa , kubr.aprekinat_tilpumu())
print('Kubr malas garums: ', kubr.malas_garums)
print('***')


#Klases "Kubs" apkašklase "Bloks"
class Bloks(Kubs): 
    def __init__(self, skaits, nosaukums, krasa, malas_garums, forma, derigums): #konstuktora izveide
        super().__init__(krasa, malas_garums) #manto no klases Kubs atribūtus

        self.skaits = skaits#izveido lauku, kuru pēc tam maina pēc nosacījumiem
        if self.skaits>=1 and self.skaits<=4:
            self.skaits = skaits
        else:
            print('Nepareiza kubu skaita vērtība!')
            skaits = 1
            self.skaits = skaits

        #nosaukums = f"{self.krasa}{self.skaits}"
        self.nosaukums = nosaukums

        skaitli = [11, 12, 13, 14, 22] #iespejamās formas vērtības
        self.derigums = derigums#izveido lauku, kuru pēc tam maina pēc nosacījumiem

        self.forma = forma #izveido lauku, kuru pēc tam maina pēc nosacījumiem
        if self.forma in skaitli:
            self.forma = forma
            self.derigums = 1
        else:
            print('Forma neatbilst nosacījumiem')
            self.derigums = 0
            self.forma = 1
        
    def tilpums(self):
        return f"{round(self.malas_garums*self.malas_garums*self.malas_garums)}"

#objektu izveide klasei Bloks
print('Oranžs objekts:')
blokg = Bloks(3, 'oranža3', 'Oranžs', 5, 13, 0) #iestata derīgumu objekta uz 0, jo programma vēlāk nomainīs ja vajag
print(blokg.nosaukums, blokg.tilpums(), 'derīgs',blokg.derigums)
print('***')

print('Zils objekts:')
blokr = Bloks(5, 'zila1', 'Zils', 7, 23, 0)
print(blokr.nosaukums, blokr.tilpums(), 'nederīgs',blokr.derigums)
print('***')

blokr.forma = 12 #iestatī formu uz derīgu skaitli
print('Mainīta forma: ')
print(blokr.nosaukums, blokr.tilpums(), 'derīgs',blokr.derigums)
