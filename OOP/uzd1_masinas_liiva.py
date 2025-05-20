from datetime import datetime #importē laiku reģistrācijas datumam

class Masinas:
    def __init__(self, zimols, modelis, pilna_masa, degvielas_veids): #konstruktors ar laukiem
        self.zimols = zimols
        self.modelis = modelis
        self.reg_datums = datetime.now().strftime('%d.%m.%Y') #iegūs šodienas datumu
        self.pilna_masa = pilna_masa
        self.degvielas_veids = degvielas_veids

    def atgriez_formatu(self): #funkcija atgriež konsolē sakārtotus datus
        print(f"Zīmols: {self.zimols}")
        print(f"Modelis: {self.modelis}")
        print(f"Reģistrācijas datums: {self.reg_datums}")
        print(f"Pilna masa: {self.pilna_masa}")
        print(f"Degvielas veids: {self.degvielas_veids}")

#objektu izveide
audi = Masinas('Audi', 'A4', 1800, 'BG') #padod parametrus, izņemot datumu, jo programma pati to iegūst
audi.atgriez_formatu() #izmanto funkciju no klases Masinas
