# 3 - В файле, содержащем фамилии студентов и их оценки, изменить на буквы в верхнем регистре тех студентов, 
# которые имеют средний балл более «4».

# Нужно перезаписать файл.
# Пример:
# Ангела Меркель 5
# Энакин Скайуокер 5
# Фредди Меркури 3
# Александр Пушкин 4

# Программа выдаст:
# АНГЕЛА МЕРКЕЛЬ 5
# ЭНАКИН СКАЙУОКЕР 5
# Фредди Меркури 3
# Александр Пушкин 4


# with open('file.txt', 'a', encoding='utf-8') as data:
#     data.write('Ангела Меркель 5\n')
#     data.write('Энакин Скайуокер 5\n')
#     data.write('Фредди Меркури 3\n')
#     data.write('Александр Пушкин 4\n')

#     # for i in data:
#     #     last_name, first_name, points = i.split()
#     # if int(points) > 4:
#     #     print(f'{last_name.upper()} {first_name.upper()}')

# data.close()



# path = 'file.txt'

# with open(path, 'w', encoding='utf-8') as file:
#     pupils = path.write().split()
# for pupil in pupils:
#     last_name, first_name, points = pupil.split()
# if int(points) > 4:
#     print(f'{last_name} {first_name}')
   
# path.close()


n = int(input("Введите через пробел: "))
nameList = []
for i in range(n):
    line1 = list(input().split())
    nameList.append((line1[1], line1[0]))
    nameList.sort(key=lambda x: -int(x[0]))
for i in nameList:
    print(i[1])
 
