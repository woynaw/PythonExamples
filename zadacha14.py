print("Введите N")
n = int(input())
rez = 2
list = []
while rez < n:
    list.append(rez)
    rez *= 2
print(*list)