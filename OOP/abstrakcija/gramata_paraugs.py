
from abc import ABC, abstractmethod

#vispārīga datu struktūra, kas nepiecišama visām grāmatām
class Gramata(ABC): #abstraktā klase ar metodi gramatas_dati
    @abstractmethod
    def gramatas_dati(self):
        pass

#izveidot 2 apakšklases, kur katra metodi (gramatas_dati) realizē citādāk

class Hobit(Gramata): #skolotāja
    def gramatas_dati(self):
        print('Hobit, 694 lpp')

class Komikss(Gramata): #es
    def gramatas_dati(self):
        print("Komiksos ir bildes")

class Vardnica(Gramata): #es
    def gramatas_dati(self):
        print('Vārdnīca skaidro citus vārdus')

gramata1 = Hobit()
gramata1.gramatas_dati()

gramata2 = Komikss()
gramata2.gramatas_dati()

gramata3 = Vardnica()
gramata3.gramatas_dati()