my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
list_index = 0
len_my_list = len(my_list)
while list_index < len_my_list:
    if my_list[list_index] > 0:
        print(my_list[list_index])
        list_index = list_index + 1
        continue
    if my_list[list_index] == 0:
        list_index = list_index + 1
        continue
    else: break

