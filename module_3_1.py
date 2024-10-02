def string_info (string_text):
    str_lenght = len(string_text)
    info_tuple = (str_lenght,string_text.upper(), string_text.lower())
    calls = count_calls()
    return info_tuple

def is_contains (string, list_to_search):
   string = string.lower()
   list_to_search_lower = [item.lower() for item in list_to_search]
   if list_to_search_lower.count(string) != 0: a = True
   else: a = False
   calls = count_calls()
   return a

def count_calls ():
   global calls
   calls = calls + 1
   return calls

calls = 0
print(string_info('orange'))
print(string_info('banan'))
print(is_contains('Alex', ['Max', 'aLeX', 'ALEX']))
print(is_contains('binom', ['BAN', 'BaNaN', 'urBAN']))
print(is_contains('bullet', ['BAN', 'BaNaN', 'urBAN']))
print(calls)