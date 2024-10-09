def print_params(a = 1, b = 'строка', c = True):
    print (a,b,c)

print_params()
print_params(12.3, 5)
print_params(5, c = 10)
values_list = [2, "test", True]
print_params(*values_list)
values_dict = {'a':1, 'b':True, 'c':"Text"}
print_params(**values_dict)
values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)