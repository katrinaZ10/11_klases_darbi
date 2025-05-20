class Rinkis:
    def __init__ (self, radiuss): #konstruktors
        self.radiuss = radiuss#lauks

    def istatit_radiusu(self, radiuss):
        #ja 0 vai negatīvs, tad uzstāda noklusējumā 1
        if radiuss <= 0:
            self.radiuss = 1
        else:
            self.radiuss = radiuss

    def izvadit_radisus(self):
        return self.radiuss

    def diametrs (self): #2piR
        return self.radiuss*2


#objektu izveide

ievade = float(input('Ievadiet rādiusu: '))
rinkis = Rinkis(ievade)
print('Riņķa rādiuss', rinkis.izvadit_radisus())
print('Riņķa diametrs', rinkis.diametrs())


