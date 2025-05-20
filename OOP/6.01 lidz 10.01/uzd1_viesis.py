#klase viesis ar konstruktoru(inicializatoru)

class Viesis:
    def __init__(self, vards, parole):
        self.vards = vards #izveido lauku
        self.parole = parole 

    def druka_vardus(self):
        print('Lietotājs', self.vards, 'izvediots.')

    def paroles_parbaude(self, parole):
        if self.parole == parole:
            print('Lietotājs', self.vards, 'parole pareiza.')

vards = 'Valdis'
parole = '12345'

#izveidot objektu
viesis1 = Viesis(vards, parole)

#objektam izsauc metodes
viesis1.druka_vardus()
viesis1.paroles_parbaude(parole)

