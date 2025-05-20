def parbaudit_vardu(vards): #Pārbauda, vai vārds vai uzvārds ir derīgs (sastāv tikai no burtiem un nav tukšs).
    return vards.isalpha()

def validet_vecumu(vecums):
    return vecums.isdigit() and int(vecums) > 0 #Pārbauda, vai vecums ir derīgs (pozitīvs skaitlis).

def pievienot_datus_failam(faila_nosaukums):
    #Pievieno datus failā pēc validācijas.
    try:
        with open(faila_nosaukums, "a", encoding="utf-8") as fails:
            vards = input("Ievadiet vārdu: ").strip()
            if not parbaudit_vardu(vards):
                print("Kļūda: Vārds drīkst saturēt tikai burtus.")
                return
                
            uzvards = input("Ievadiet uzvārdu: ").strip()
            if not parbaudit_vardu(uzvards):
                print("Kļūda: Uzvārds drīkst saturēt tikai burtus.")
                return

            vecums = input("Ievadiet vecumu: ").strip()
            if not validet_vecumu(vecums):
                print("Kļūda: Vecumam jābūt pozitīvam veselam skaitlim.")
                return

            fails.write(f"{vards},{uzvards},{vecums}\n")
        print("Dati veiksmīgi pievienoti failam.")
    except Exception as e:
        print(f"Kļūda, saglabājot datus failā: {e}")

def paradit_datus(faila_nosaukums):
    #Parāda datus no faila, ja tāds eksistē un nav tukšs.
    try:
        with open(faila_nosaukums, "r", encoding="utf-8") as fails:
            dati = fails.readlines()

        if not dati:
            print("Fails ir tukšs. Lūdzu, pievienojiet datus vispirms.")
        else:
            print("\nDati no faila:")
            for ieraksts in dati:
                print(ieraksts.strip())
    except FileNotFoundError:
        print(f"Fails '{faila_nosaukums}' nepastāv. Lūdzu, pievienojiet datus vispirms.")

def iegut_vecumu_no_datiem(ieraksts):
    #Izvelk vecumu no datu ieraksta.
    try:
        vecums = int(ieraksts.strip().split(",")[-1])
        return vecums
    except (IndexError, ValueError):
        return 0  # Ja formāts nav pareizs, atgriež 0

def sakartot_un_paradit_datus(faila_nosaukums):
    #Sakārto datus pēc vecuma un parāda tos konsolē.
    try:
        with open(faila_nosaukums, "r", encoding="utf-8") as fails:
            dati = fails.readlines()

        if not dati:
            print("Fails ir tukšs. Lūdzu, pievienojiet datus vispirms.")
        else:
            # Kārtošana pēc vecuma
            sakartoti_dati = sorted(dati, key=iegut_vecumu_no_datiem)

            print("\nDati, sakārtoti pēc vecuma:")
            for ieraksts in sakartoti_dati:
                print(ieraksts.strip())
    except FileNotFoundError:
        print(f"Fails '{faila_nosaukums}' nepastāv. Lūdzu, pievienojiet datus vispirms.")

def izvelne():
    #Parāda izvēlni un apstrādā lietotāja izvēli.=
    faila_nosaukums = "dati.txt"

    while True:
        print("\nIzvēlieties opciju:")
        print("1 - Pievienot datus")
        print("2 - Parādīt datus")
        print("3 - Parādīt sakārtotus datus pēc vecuma")
        print("4 - Iziet")

        izvēle = input("Izvēle: ")

        if izvēle == "1":
            pievienot_datus_failam(faila_nosaukums)
        elif izvēle == "2":
            paradit_datus(faila_nosaukums)
        elif izvēle == "3":
            sakartot_un_paradit_datus(faila_nosaukums)
        elif izvēle == "4":
            print("Izvade tiek pārtraukta.")
            break
        else:
            print("Nepareiza izvēle. Lūdzu, mēģiniet vēlreiz.")

# Galvenā programmas izsaukšana
izvelne()
#faila_nosaukums tiek padots kā arguments, lai funkcijas būtu atkārtoti izmantojamas ar citiem failiem.
#Katra datu rinda ir atdalīta ar komatiem (vārds,uzvārds,vecums), kas atvieglo datu apstrādi.
#sakartot_un_paradit_datus() izmanto iegut_vecumu_no_datiem() funkciju, lai iegūtu vecumu no katras rindas un sakārtotu pēc tā.