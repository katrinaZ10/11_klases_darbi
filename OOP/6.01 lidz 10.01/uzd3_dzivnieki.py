class Dzivnieks:
    def __init__(self, vards, skana):
        self.vards = vards
        self.skana = skana

    def izdod_skanu(self):
        return f"{self.vards} saka {self.skana}!"

#objekti
suns = Dzivnieks('Suns', 'Vau')
vista = Dzivnieks('Vista', 'Ko ko')
gailis = Dzivnieks('Gailis', 'Kirerigūu')

print(suns.izdod_skanu())
print(vista.izdod_skanu())
print(gailis.izdod_skanu())


