
class Skolotajs:
    def __init__(self, vards, prieksmets): #konstruktors
        self.vards = vards #lauki / atribūti
        self.prieksmets = prieksmets

    def iepazistiniArSevi(self):
        print( f"Sveiki, mani sauc {self.vards}")
    
    def izliktVertejumu(self, atzime):
        if atzime < 5:
            return f"Priekšmets {self.prieksmets} NAV nokārtots!"
        else:
            return f"Priekšmets {self.prieksmets} IR nokārtots!"

#objekti, instatēšana (latviski un jāzin)
#objektam ir uzvedība

rinalds = Skolotajs('Rinalds', 'Matemātika')
sandra = Skolotajs('Sandra', 'Literatūra')

rinalds.iepazistiniArSevi()
print(rinalds.izliktVertejumu(8))

sandra.iepazistiniArSevi()
print(sandra.izliktVertejumu(3))
