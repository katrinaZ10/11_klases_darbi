class SportaKlubs:
    def __init__(self):
        #inicalizē tukšus atribūtus, jo ir lietotāja ievade 
        self.nosaukums = ""
        self.vieta = ""
        self.biedru_skaits = 0

    def ievadit_datus(self): #metode datu ievadei 
        #self kā atsauce uz objektu
        self.nosaukums = input("Ievadiet kluba nosaukumu: ")
        self.vieta = input("Ievadiet atrašanās vietu: ")
        while True:
            try:
                self.biedru_skaits = int(input("Ievadiet aktīvo biedru skaitu: "))
                break
            except ValueError:
                print("Lūdzu ievadiet derīgu skaitli!")

    #vienkārša metode datu izvadei
    def izvadit_datus(self):
        print(f"Sporta klubs: {self.nosaukums}")
        print(f"Atrašanās vieta: {self.vieta}")
        print(f"Aktīvo biedru skaits: {self.biedru_skaits}")

#Izveidots sporta kluba objektu un izmantotas datu ievades un izvades metodes
klubs = SportaKlubs()
klubs.ievadit_datus()
klubs.izvadit_datus()
