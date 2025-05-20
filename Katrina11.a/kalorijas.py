# Kopējā summa kalorijām
kalorijas = 0

def ievadi_pareizu_skaitli(teksts): #ievades pārbaude
    while True:
        skaitlis = float(input(teksts))
        if skaitlis > 0:
            return skaitlis
        else:
            print('Nepareiza ievade! Lūdzu ievadiet skaitli, kas lielāks par 0.')

def ievadi_pareizu_aktivitates_limenis(teksts):#ievades pārbaude
    while True:
        aktivitate = input(teksts)
        if aktivitate in ["z", "v", "a"]:
            return aktivitate
        else:
            print('Nepareiza ievade! Lūdzu ievadiet vai nu "z", "v", vai arī "a"')

def ievadi_pareizu_dzimumu(teksts):#ievades pārbaude
    while True:
        dzimums = input(teksts)
        if dzimums in ["v", "s"]:
            return dzimums
        else:
            print('Nepareiza ievade! Lūdzu ievadiet vai nu "v", vai arī "s"')

# Aprēķina un atgriež apēstās kalorijas vienam ēdienam
def ievadi_edu_datus():
    nosaukums = input("Ievadiet ēdiena nosaukumu: ")
    kalorijas_uz_100g = ievadi_pareizu_skaitli("Ievadiet kalorijas uz 100 gramiem: ")
    daudzums = ievadi_pareizu_skaitli("Ievadi apēsto ēdiena daudzumu [g]: ")
    return (kalorijas_uz_100g / 100 * daudzums)

def aprekinat_ieteikto_kaloriju_daudzumu():
    svars = ievadi_pareizu_skaitli("Ievadiet savu svaru [kg]: ")
    vecums = int(ievadi_pareizu_skaitli("Ievadiet savu vecumu [gadi]: "))
    dzimums = ievadi_pareizu_dzimumu("Ievadiet savu dzimumu [v - vīrietis/s - sieviete]: ")
    aktivitates_limenis = ievadi_pareizu_aktivitates_limenis("Ievadiet savu aktivitātes līmeni [z - zems, v - vidējs, a - augsts]: ")
    if dzimums == "v":
        if aktivitates_limenis == "z":
            return (9.65 * svars) + (573 * 1.80) - (5.08 * vecums) + 200
        elif aktivitates_limenis == "v":
            return (9.65 * svars) + (573 * 1.80) - (5.08 * vecums) + 260
        elif aktivitates_limenis == "a":
            return (9.65 * svars) + (573 * 1.80) - (5.08 * vecums) + 300
    elif dzimums == "s":
        if aktivitates_limenis == "z":
            return (7.38 * svars) + (607 * 1.70) - (2.31 * vecums) + 43
        elif aktivitates_limenis == "v":
            return (7.38 * svars) + (607 * 1.70) - (2.31 * vecums) + 60
        elif aktivitates_limenis == "a":
            return (7.38 * svars) + (607 * 1.70) - (2.31 * vecums) + 100

#def sniegt_parskatu()