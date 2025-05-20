#bāzes klases Persona ar laukiem vārds, vecums u metodi kas šos datus idzrukā

class Persona:
    def __init__(self, vards, vecums):
        self.vards = vards
        self.vecums = vecums

    def izdruka(self):
        print(f"Studenta vārds: {self.vards}\nStudenta vecums: {self.vecums}")



#atvasinātā klase Students, kas manto abus divus laukus un pievienot specifikso lauku "kurss"
class Students(Persona):
    def __init__(self, vards, vecums, kurss):
        super().__init__(vards, vecums)
        self.kurss = kurss
        #metodes pārrakstīšana

    def izdruka(self):
        super().izdruka()
        print('Studenta kurss: ', self.kurss)

#izveidot katria klasei vienu objektu
persona1 = Persona('Romija', 32)
print(persona1.izdruka())

students1 = Students('Pipars', 34575297, 4)
print(students1.izdruka())

super(Students, students1).izdruka()