numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in numbers: # проверка на наличие 1 в списке и удаление 1 (1 не простое и не составное число)
    if i == 1:
        numbers.remove(i)
#print(numbers)
for i in numbers:
    for j in range(2,i):
         if i % j == 0: # прооверка, если число не ппостое (есть делитель)
            not_primes.append(i)
            break
    else: primes.append(i) # иначе - число простое
print(primes)
print(not_primes)
