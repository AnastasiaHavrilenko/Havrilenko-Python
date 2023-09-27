n = 7
array = [[0] * n for _ in range(n)]

# Заповнення масиву
for i in range(n):
    for j in range(i+1):
        array[j-i+6][i] = j+1

# Вивід заповненого массива:
for row in array:
    print(" ".join(map(str, row)))
