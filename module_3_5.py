def get_multiplied_digits (number):
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) == 1:
        return first
    if str_number[-1] == '0' and len(str_number) == 2:
        return first
    elif str_number[-1] == '0' and len(str_number) > 2:
           str_number = str_number.replace('0','1')
           return first * get_multiplied_digits(int(str_number[1:]))
    else:
       result = first * get_multiplied_digits(int(str_number[1:]))
       return result


result = get_multiplied_digits(502004000000)
print(result)