
#definē klasi Dzivnieks, kas ir saistīts ar kāju skaitu
class Dzivnieks:
    def __init__(self, kaju_sk=0):
        self.kaju_sk = kaju_sk

    @classmethod #izmanto objektu izveidošanu ar notiektu kāju skaitu
    def putns(kajas):
        return kajas(2)

    @classmethod #izmanto objektu izveidošanu ar notiektu kāju skaitu
    def majlops(kajas):
        return kajas(4)

    @classmethod #izmanto objektu izveidošanu ar notiektu kāju skaitu
    def astonkajis(kajas):
        return kajas(8)

    @classmethod #izmanto objektu izveidošanu ar notiektu kāju skaitu
    def simtkajis(kajas):
        return kajas(100)

    #metode, kas izdrukā kāju skaitu
    def izdruka_kaju_skaitu(self):
        print(self.kaju_sk)

#objektus(instance)
odze = Dzivnieks()
zoss = Dzivnieks.putns()
kaza = Dzivnieks.majlops()
astonkajis = Dzivnieks.astonkajis()
simtkajis = Dzivnieks.simtkajis()

odze.izdruka_kaju_skaitu()
zoss.izdruka_kaju_skaitu()
kaza.izdruka_kaju_skaitu()
astonkajis.izdruka_kaju_skaitu()
simtkajis.izdruka_kaju_skaitu()