#Дан список A размера N. Вывести его элементы в следующем порядке: A1, AN, A2,
#AN-1, A3, AN-2, ….


A = [1, 2, 3, 4, 5]

n = len(A)
result = []
try:
    for i in range(n // 2):
        result.append(A[i])
        result.append(A[n - i - 1])
    if n % 2 != 0:
        result.append(A[n // 2])
except:
    print("something went wrong")

print(result)
