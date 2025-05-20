'''#saglabāt datus sarakstā
names = []
for i in range(3):
    names.append(input('Whats your name?: '))
    #atgriezīsim kārtotus
for name in sorted(names):
    print(f"Hello,{name}")
    #būs jāzin kārtošana ar failiem

#informāciju no konsoles ieraksta failā
name = input('Whats your name?: ')
file = open("names.txt", "a", encoding='utf8') #w izveido un ieraksta datus
#a režīmā arī izveido failu, bet info pievieno klāt
file.write(f"{name}\n")
file.close()# ja izmanto file.open tad ir jāizver (file.close) viņš arī ciet\


#lieto contex manager (fails nav jāaizver)
name = input('Whats your name?: ')
with open("names.txt", "a", encoding='utf8') as file:
    file.write(f"{name}\n")

#nolasa info no faila
with open("names.txt", encoding='utf8' ) as file:#e ir nokusējuma režīms viņu var neraskstīt
    for line in file:
        print('Hello,', line.rstrip())#rstrip noņem liekās rindiņas un liekās atstarpes
'''

#atgriezt sakārtotus datus no faila
names = []
with open("names.txt", encoding='utf8') as file:
    for line in file:
        names.append(line.rstrip())
    #atgriezīsim kārtotus
for name in sorted(names):
    print(f"Hello, {name}")

#ieskaitē būs datu kārtošana
