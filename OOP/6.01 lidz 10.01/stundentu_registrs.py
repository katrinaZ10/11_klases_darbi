
class Students:

    def __init__(self): #konstruktors
        self.vards = "" #tukšas pēdiņas, jo tiks lietota input funkcija
        self.uzvards = ""
        self.vecums = 0 #vecums = 0, jo lietotājs pat vaiks ievadi (input)
        self.kurss = 0

    def datu_ievade(self): #funkcija iegūs datus no lietotāja
        
        self.vards = input('Ievadiet studenta vārdu: ')
        self.uzvards = input('Ieavdiet studenta uzvārdu: ')

        while True:
            try:
                self.vecums = int(input('Ievadiet stundenta vecumu: '))
                if self.vecums >= 18:
                    break
                else:
                    print('Kļūda: Nepareiza vecuma ievade! ')

            except ValueError:
                print('Kļūda: Nepraiza datu ievade!')

        while True:
            try:
                kursi = [1, 2, 3, 4] #iespējamie kursi, kuros pārbaudīs lietotāja ievadi
                self.kurss = int(input('Ievadiet kursa numuru: '))
                if self.kurss in kursi:
                    break
                else:
                    print('Kļūda: Nepareiza kursa ievade!')

            except ValueError:
                print('Kļūda: Nepraiza datu ievade!')

    def parada_datus(self): #funkcija uz konsole parādīt iegūtos datus
        print(f"\nStudent: {self.vards} {self.uzvards}\nVecums: {self.vecums}\nKurss: {self.kurss}")

#objekta izveide

students1 = Students()
students1.datu_ievade()
students1.parada_datus()

