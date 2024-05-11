# Дан список размера N. Осуществить циклический сдвиг элементов списка влево на
# одну позицию (при этом AN перейдет в AN-1, AN-1 — в AN-2, . . ., A1 — в AN)

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

last_element = lst[0]
try:
    for i in range(len(lst) - 1):
        lst[i] = lst[i + 1]
    lst[-1] = last_element
except:
    print("something went wrong")

print(lst)
