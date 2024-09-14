grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]] #//исходный список оценок в алфавитном порядке
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'} # //исходное множество студентов
sum_list_grades=list(map(sum, grades)) # // расчет суммарного балла каждого студента
len_list_grades=list(map(len,grades)) # // расчет количества оценок, ролученных кажддым студеном
print(sum_list_grades, len_list_grades) # // контрольный вывод
avr_list=[int(s) / int(l) for s,l in zip(sum_list_grades, len_list_grades)] # // расчет среднего балла каждого студента
print(avr_list) # // контрольный вывод
students_list=list(students) # // преобразование множества в список
students_list.sort() # // сортировка списка студентов по алфавиту
print(students_list) # // контрольный вывод
students_dict=dict(zip(students_list,avr_list)) # // создание итогового словаря
print(students_dict) # //  вывод словаря в консоль
