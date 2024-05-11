#Дано вещественное число А и целое число N (>0). Используя один цикл, найти сумму
# 1 + A + A**2 + A**3 + ... +A**n
total = 0

# Exception Handling
while True:
    try:
        a = float(input("input float number"))
        n = int(input("input exponent number"))
        if n <= 0:
            print("exponent must be more than zero")
            continue
    except ValueError:
        print("something went wrong")
        continue
    break

# Calculation
for i in range(0, n+1):
    total = total + a**i

print(total)
