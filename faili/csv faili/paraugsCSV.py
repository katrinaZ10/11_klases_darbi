import csv
'''#izveidots csv failu un ļauj rastīt datus
with open("students0.csv", "w", encoding='utf8', newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Name", "House"])# pievieno kolonnu nosaukums

    #iegūst datus no lietotāja
    while True:
        name = input("Enter name and house(type 'okey' to finish): ")
        if name.lower()== 'okey':
            break
        studenHouse = input(f"Enter {name}'s house: ")
        writer.writerow([name, studenHouse])
        print(f"{name} has been added!")'''

#nolasīt informāciju no csv faila

students = []

with open("students0.csv", encoding='utf8') as file:
    for line in file: #cikla mainīgais katrā iterācija iegūst rindiņas saturu kā txt failu
        name, house = line.rstrip().split(",") #noņem liekos simbols rindas beigās, ar split sadala tekstu
        #izvada formatētu tekstu
        students.append(f"{name} is in {house}. ")

for students in sorted(students):
    print(students)

#sakārtot informāciju no csv faila



