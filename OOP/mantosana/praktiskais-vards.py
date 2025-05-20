#Praktiskais darbs: Mantošana un polimorfisms

#Uzdevums: Izveidot klases un demonstrēt mantošanu un polimorfismu, izmantojot dotās vadlīnijas.

#1. Izveidot klasi "Transportlidzeklis", kura satur šādas īpašības un metodes:
#īpašība "nosaukums" (piemēram, "Automašīna" vai "Velosipēds")
#īpašība "atrums" (vesels skaitlis, kas norāda maksimālo ātrumu km/h)
#metode "info", kas izvada transportlīdzekļa nosaukumu un ātrumu

#2. Izveidot divas klases, kas mantotu "Transportlidzeklis":
#"Automašīna", kas pievieno īpašību "durvju_skaits" un pārdefinē metodi "info", lai pievienotu šo informāciju.
#"Velosipēds", kas pievieno īpašību "tips" (piemēram, "kalnu" vai "pilsētas") un arī pārdefinē metodi "info".

#3.Demonstrēt polimorfismu(metožu pārrakstīšana), izveidojot sarakstu ar dažādiem transportlīdzekļu objektiem un izsaucot metodi "info" katram no tiem.

#Aizpildīt tukšās vietas!

#Šeit ir sākuma kods:

class Transportlidzeklis:
    def __init__(self, nosaukums, atrums):
        self.nosaukums = nosaukums
        self.atrums = atrums

    def info(self):
        print(f"{self.nosaukums} ar maksimālo ātrumu {self.atrums} km/h")

#Pievieno savu kodu šeit:

#1.Izveido klasi Automasinaa, kas mantos klasi Transportlidzeklis un pievieno īpašību durvju_skaits
class Masina(Transportlidzeklis):
    def __init__(self, nosaukums, atrums, durvju_sk):
        super().__init__(nosaukums, atrums)
        self.durvju_sk = durvju_sk

    def info(self):
        super().info()
        print('Durvju skaits: ', self.durvju_sk)


#2.Izveido klasi Velosipeds, kas mantos klasi Transportlidzeklis un pievieno īpašību tips
class Ritenis(Transportlidzeklis):
    def __init__(self, nosaukums, atrums, tips):
        super().__init__(nosaukums, atrums)
        self.tips = tips

    def info(self):
        super().info()
        print('Velosipēda tips: ', self.tips)


#3.Izveido dažādus transportlīdzekļu objektus un pievieno tos sarakstam
transportlidzekli = [Masina("Volvo", 180, 4), Ritenis("Trek", 70, "Kalnu"), Masina("Porche", 270, 2), Masina('Toyota', 210, 4)]

#transportlidzekli.append(...)
transportlidzekli.append(Ritenis('Orbea', 60, 'Pilsētas'))
#4.Izsauc metodi info katram transportlīdzeklim
for t in transportlidzekli:
    t.info()  
    print('-'*12)

