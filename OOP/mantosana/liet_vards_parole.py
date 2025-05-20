
class Viesis:
    def __init__(self, vards, parole):
        self.vards = vards
        self.parole = parole

    #izdrukā info par iaveidotu lietotāju
    def druka_vardu(self):
        print(f"Lietotājs {self.vards} ir izveidots")
        
    def parbada_paroli(self, parole):
        #pārbauda, vai paroles sakrīt 
        if self.parole == parole:
            print(f"Lietotāja {self.vards} parole ir pareiza!")
        else:
            print('Parole ir nepareiza!')

#klase Darbinieks manto no klases Viesis 
#metode druka_vardu() izprientē info par adminstratoru

class Darbinieks(Viesis):
    def __init__(self, vards, parole):
        super().__init__(vards, parole)
    
    def druka_vardu(self):
        print(f"Administrators {self.vards} ir izveidots")

#testa dati
vards1 = 'Lora'
parole1 = 'Suns'

vards2 = 'Pipars'
parole2 = 'Kakis'

#izveidot objaktu klasei Viesis
viesis1 = Viesis(vards1, parole1)
viesis1.druka_vardu()
viesis1.parbada_paroli(parole1)

viesis2 = Darbinieks(vards2, parole2)
viesis2.druka_vardu()
viesis2.parbada_paroli(parole2)
