
class Persona:
    def __init__(self, vards, uzvards, epasts): #bāzes klase
        self.vards = vards
        self.uzvards = uzvards
        self.epasts = epasts

    def druka_vardsu(self):
        print('Šo personu sauc: ', self.vards)

class Skolens(Persona): #atvasinātā klase
    def __init__(self, vards, uzvards, epasts, vid_atzime):
        super().__init__(vards, uzvards, epasts) #automātiski izsauc metodes no Persona
        self.vid_atzime = vid_atzime

    def macities(self):
        self.vid_atzime += 0.1

class Skolotajs(Persona):
    def __init__(self, vards, uzvards, epasts, macibu_prieksmets):
        super().__init__(vards, uzvards, epasts) #automātiski izsauc metodes no Persona
        self.macibu_prieksmets = macibu_prieksmets #pieveino jaunu lauku

    def macit_stundu(self):
        print('Mācu: ', self.macibu_prieksmets)

#izveidot objektus abām atvasinājuma klasēm
skolens1 = Skolens('Jānis', 'Bērziņš', 'janis.berzins@svg.lv', 8.5)
print(skolens1.epasts)

skolens1.macities()
print(skolens1.vid_atzime)

skolotajs1 = Skolotajs('Romija', 'Suhanova', 'romijaa@svg.lv', 'Bioķīmija')
print(skolotajs1.macit_stundu())