class Gramata:
    def __init__(self, nosaukums, autors, gads, lappuses, cena):
        #atribūtu(lauku) inicializācija
        self.nosaukums = nosaukums
        self.autors = autors
        self.gads = gads
        self.lappuses = lappuses
        self.cena = cena

    #izveidot metodi, kas izvada informāciju par grāmatu
    def izvadit_info(self):
        print(f"Grāmatas nosaukums: {self.nosaukums}")
        print(f"Autors: {self.autors}")
        print(f"Izdošanas gads: {self.gads}")
        print(f"Lappušu skaits: {self.lappuses}")
        print(f"Cena: {self.cena} EUR")

#objekts ar testa datiem
gramata = Gramata("1984", "George Orwell", 1949, 328, 9.99)
gramata.izvadit_info()
