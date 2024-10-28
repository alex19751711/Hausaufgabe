n = 20
# определение списка кратных пар
list1 = []
for i in range (1,n+1):
    for j in range (1,n+1):
        if i == j: continue
        if j == i: continue
        if n % (i+j) == 0:
           list1.append(i)
           list1.append(j)
           if n % (i+j) != 0:
            continue
# формирование списка уникальных пар
pairs = []
unique = []
for k in range(0, len(list1), 2):
        if k + 1 < len(list1):
            # Создаем пару и сортируем ее
            pair = list(sorted((list1[k], list1[k + 1])))
            if pair in pairs:
                unique.remove(pair)  # Удаляем пару, если она уже встречалась
            else:
                pairs.append(pair)
                unique.append(pair)  # Добавляем уникальную пару
#print(list(unique))
#print(pairs)
#финальный вывод отобранных пар в виде строки
chiffre = []
for group in pairs:
    chiffre += group
#print(chiffre)
print(n)
print(''.join(map(str, chiffre)))