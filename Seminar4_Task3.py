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
# Фредди Меркьюри 3
# Александр Пушкин 4


from typing import List

def list_changed(spisok: List[str], accept: str) -> str:
    list_file = ' '
    for student in spisok:
        if student.count(accept):
            student = student.upper()
        string = student + "\n"
        list_file += string
    return list_file




students_list = open('file.txt', 'r', encoding='utf-8')
new_list = students_list.read().split('\n')
students_list.close()

rewriten_list = list_changed(new_list, accept = '5')


students_list = open('file.txt', 'w', encoding='utf-8')
students_list.write(rewriten_list)
students_list.close()
