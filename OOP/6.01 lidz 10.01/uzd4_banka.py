#izveidot klasi BankasKonts
#ielikst 2 atribūtus - klienta vārds un atlikums
#klasē ir 2 metodes - imaksa(summa) - palielinās konta atlikumu ar norādīto summu
#summmu norādīs pie izsaukšanas
#metode izņemt(summa) - samazina konta atlikumu par norādīto summu, ja pietiek (summa > atribūtu)
#objekti - klientam Laura sākumā ir 100 eiro / iemaksā 50, pārbauda atlikumu
#izņem 30, pēc tam mēģinā izņemt 200, lai notestētu gadījumu, kad nav līdzekļu

class BankasKonts:
    def __init__(self, vards, atlikums): #konstruktors ar 2 parametriem
        self.vards = vards
        self.atlikums = atlikums

    def iemaksa(self, nauda):
        self.atlikums+=nauda #palielina atlikumu
        return f"Iemaksāti {nauda} EUR. Jaunais atlikums: {self.atlikums}"


    def iznemt(self, nauda):
        #pārbauda vai kontā pietiek līdzekļu
        if nauda > self.atlikums:
            return 'Nepietiek līdzekļu!'

        self.atlikums -= nauda #samazina konta atlikumu
        return f"Iemaksāti {nauda} EUR. Jaunais atlikums: {self.atlikums}"

#objekts
konts = BankasKonts('Laura', 100)

print(konts.iemaksa(50))
print(konts.iznemt(30))
print(konts.iznemt(200))

