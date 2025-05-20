#uz ekrāna izdrukāt visus nepāra skaitļus no lietotāja ievadītā diapazonas
sakums = int(input('Ievadiet sākumu: '))
beigas = int(input('Ievadiet beigas: '))

for skaitlis in range(sakums, beigas+1):
    if skaitlis%2 != 0:
        print(skaitlis)


