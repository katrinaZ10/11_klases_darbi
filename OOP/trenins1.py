class Students:
    def __init__(self): #konstruktoram nav parametru-sākotnējie dati nav zināmi
        self.vards = ""  
        self.uzvards = "" #vērtības vēlāk aizpilda, izmantojot ievades metodi
        self.vecums = 0
        self.kurss = 0  #ja izmanto input, tad nav nepieciešams padot parametrus konstruktoram, 
        #jo datus var ievadīt un piešķirt klases atribūtiem vēlāk, izmantojot metodes 
        
#self ļauj piešķirt un izmantot klases atribūtus, kas pieder konkrētai objekta instancei
#bez self programma nezinātu, ka šie atribūti pieder konkrētajam objektam
    def ievadit_datus(self):
        self.vards = input("Ievadiet studenta vārdu: ") 
        self.uzvards = input("Ievadiet studenta uzvārdu: ")
        while True: 
            try:
                self.vecums = int(input("Ievadiet studenta vecumu: "))  
                if self.vecums >= 18:
                    break
                else:
                    print("Vecumam jābūt vismaz 18!")
            except ValueError: #ja ievada kaut ko, kas nav skaitlis
                print("Lūdzu ievadiet derīgu vecumu!") 
        while True:
            try:
                self.kurss = int(input("Ievadiet kursa numuru (1-4): "))
                if 1 <= self.kurss <= 4:
                    break
                else:
                    print("Kurss jābūt no 1 līdz 4!")
            except ValueError:
                print("Lūdzu ievadiet derīgu kursa numuru!")

    def izvadit_datus(self):  
        print(f"Vārds: {self.vards}, Uzvārds: {self.uzvards}, Vecums: {self.vecums}, Kurss: {self.kurss}")

students = Students() #objekts klasei Students, argumentu nav, jo konstruktoram nav parametru
students.ievadit_datus()
students.izvadit_datus()


'''Python objektorientētajā programmēšanā atslēgvārds self tiek izmantots, lai 
atsauktos uz pašreizējo klases instanci. Tas ir nepieciešams, 
lai piekļūtu objekta atribūtiem un metodēm katrā klases instancē atsevišķi.'''


#izveido konstruktoru ar parametriem, uzreiz nododot vērtības objektam
'''class Students:
    def __init__(self, vards, uzvards, vecums, kurss):
        self.vards = vards
        self.uzvards = uzvards
        self.vecums = vecums
        self.kurss = kurss

    def izvadit_datus(self):
        print(f"Vārds: {self.vards}, Uzvārds: {self.uzvards}, Vecums: {self.vecums}, Kurss: {self.kurss}")
        
# Objekts tiek izveidots uzreiz ar vērtībām
students = Students("Jānis", "Bērziņš", 20, 3)
students.izvadit_datus()'''