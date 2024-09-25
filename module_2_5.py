def get_matrix(n,m, value):
    matrix = []
    for i in range (n):
        list_strings = []
        matrix.append(list_strings)
        for j in range (m):
            list_strings.append(value)
    result = matrix
    return result

result1 = get_matrix(2,2,10)
result2 = get_matrix(3,5,42)
result3 = get_matrix(4,2,13)
print(result1)
print(result2)
print(result3)