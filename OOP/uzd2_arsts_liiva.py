
class Doktorats:

    def __init__(self): #padod tikai self atribūtu, jo pārējos ievadīs lietotājs
        #laukiem nav doti parametri, jo lietot'\ajs tos iestatīs/ievadīs pats
        self.nosaukums = ''
        self.pacientu_skaits = 0 

    def liet_ievade(self):

        self.nosaukums = input('Ievadiet doktorāta nosaukumu: ')

        while True: #cikls ļauj lietotājam mēģināt vairākkārt ievadīt pareizi
            try: #funkcija pārbauda vai ir ievadīts skaitlis

                self.pacientu_skaits = int(input("Ievadiet doktorāta pacientu skaitu: "))
                break #ja ir pareiza ievade programma iziet no cikla un turpina tālāk
            
            except ValueError: #nepareizas ievades gadījumā parāda lietotājam ka ir kļūda
                print("Kļūda: Ievadiet skaitli!")

    def datu_izvade(self): #funkcija uz konsloes 'smuki' izvadīs iegūtos datus
        print(f"Doktorāts {self.nosaukums} apkalpo {self.pacientu_skaits} pacientus.")

#objekta veidošana
doktorats1 = Doktorats() #izsauc klasi doktorats no kuras tiks ņemtas funkcijas
doktorats1.liet_ievade()#izsauc funkciju no klases Doktorats
doktorats1.datu_izvade()#izsauc funkciju no klases Doktorats

