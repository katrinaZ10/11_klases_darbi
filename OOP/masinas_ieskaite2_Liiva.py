
#A uzdevums- bāzes klases izveide
class Masina: #bāzes klases izveide
    def __init__(self, marka, modelis, gads): #klases konstruktors ar atribūtiem
        #lauku izveide
        self.marka = marka 
        self.modelis = modelis
        self.gads = gads

    #B uzdevums- metodes veidošanas
    def uzsakt(self): #metode konsolē parādīt ka auto ir uzsācis darbību
        print(f"{self.marka} {self.modelis} sāk darboties!")

    def apstaties(self): #metode konsolē parādīt ka auto ir beidzis darbību
        print(f"{self.marka} {self.modelis} ir apstādināta!")

    def info_par_auto(self): #metode konsolē parādīs iformāciju par mašīnu, un izmantojot 'self' tā piekļūs konstruktorā deklerētajiem laukiem
        print(f"Automašīnas marka: {self.marka}")
        print(f"Automašīnas modelis: {self.modelis}")
        print(f"Automašīnas gads: {self.gads}")

#C uzdevums - objekta izveide klasei Masina
auto = Masina('Audi', 'A8', 2017) #objekta izveide
auto.info_par_auto() #izsauc metodi izmantojot objekta  vērtības
auto.uzsakt() #izsauc metodi izmantojot objekta  vērtības
auto.apstaties() #izsauc metodi izmantojot objekta  vērtības
print() #šis print ieliek atstapri strap pārējo informāciju ko parādīs kosolē, lai ir vieglāk pārskatīt


#D uzdevums - mantotāj klase Elektro_auto
class Elektro_auto(Masina):
    #E uzdevums - iestatīšana akumulatoram uz 100
    def __init__(self, marka, modelis, gads, akumulatora_ietilp=100): #konstruktors, un pie jaunā atribūta 'akumulatora_ietilp' ir deklerāta tā pamat vērtība 100
        super().__init__(marka, modelis, gads) #ar super metode manto no vecāka klases, šajā gadījuma klases Masina
        self.akumulatora_ietilp = akumulatora_ietilp #lauka izveide, atbilstoši mantotāj klasei

    #F uzdevums - metodes mantošana
    def uzsakt(self): #metodes pārakstīšana, polimorfisms
        if self.akumulatora_ietilp >=20: #pārbauda vai auto ir pietiekami uzlēdāts, ja nē programma neļauj uzsākt kustību
            print(f"{self.marka} {self.modelis} sāk darboties. Akumulators: {self.akumulatora_ietilp}%")
        else:
            print(f"{self.marka} {self.modelis} nevar sākt darboties, jo akumulamtors ir pārāk zems : {self.akumulatora_ietilp}%")

    #G uzdevums - metodes mantošana un papildināšana
    def info_par_auto(self): #metode atgriež konsolē infromāciju par  elektrisko mašīnu
        super().info_par_auto() # funkcija super() iegūst no vecāku klase metodi, nav jāpāraksta
        print(f"Akulumatora ietilpība: {self.akumulatora_ietilp} kWh") #pieveinots jaunā lauka informācija konsoles parādīšanai
        


#H uzdevums - objekta izveide ar pietiekami uzlādi
auto2 = Elektro_auto('Ora', 'Funky cat', 2024) #nav jādod akumulatora līmenis, jo ir jau iestatīts uz 100
auto2.info_par_auto() #izsauc metodi izmantojot objekta  vērtības
auto2.uzsakt() #izsauc metodi izmantojot objekta vērtības

#I uzdevums - Iestata uz nepietiekamu uzlādi
auto2 = Elektro_auto('Ora', 'Funky cat', 2024, 15) #iestata auto2 uzlādes līmeni uz nepietiekamu
auto2.uzsakt() #izsauc metodi izmantojot objekta  vērtības
print()#šis print ieliek atstapri strap pārējo informāciju ko parādīs kosolē, lai ir vieglāk pārskatīt


#J uzdevums - jauna manotāj klase 'Degvielas_auto'
class Degvielas_auto(Masina):
    #K uzdevums - iestatīt bākas degvielas līmeni uz 100
    def __init__(self, marka, modelis, gads, bakas_tilpums= 100):
        super().__init__(marka, modelis, gads)
        self.bakas_tilpums = bakas_tilpums #jauna lauka izveide, atbilstoši mantotāj klasei

    def uzsakt(self): #metodes pārakstīšana, polimorfisms
        if self.bakas_tilpums >=10: #pārbauda vai auto ir pietiekami uzlēdāts, ja nē programma neļauj uzsākt kustību
            print(f"{self.marka} {self.modelis} sāk darboties. Degvielas līmenis: {self.bakas_tilpums}%")
        else:
            print(f"{self.marka} {self.modelis} nevar sākt darboties, jo degvielas līmens ir pārāk zems : {self.bakas_tilpums}%")

    #M uzdevums - metodes mantošana un papildināšana
    def info_par_auto(self):
        super().info_par_auto() # funkcija super() iegūst no vecāku klase metodi, nav jāpāraksta
        print(f"Bākas tilpums: {self.bakas_tilpums} litri") #pieveinots jaunā lauka informācija konsoles parādīšanai


#N uzdevums - objektu izveide ar pietiekmi bendzīnu
auto3 = Degvielas_auto('Toyota', 'Land Cruiser', 2018) #nav jādod degvielas līmenis, jo ir jau iestatīts uz 100
auto3.info_par_auto() #izsauc metodi izmantojot objekta  vērtības
auto3.uzsakt() #izsauc metodi izmantojot objekta  vērtības
#print()#šis print ieliek atstapri strap pārējo informāciju ko parādīs kosolē, lai ir vieglāk pārskatīt
        
#O uzdevums - iestata bendzīna līmeni uz nepietiekamu
auto3 = Degvielas_auto('Toyota', 'Land Cruiser', 2018, 5) #istata auto3 degvielu uz nepietiekamu
auto3.uzsakt() #izsauc metodi izmantojot objekta  vērtības
print()#šis print ieliek atstapri strap pārējo informāciju ko parādīs kosolē, lai ir vieglāk pārskatīt

