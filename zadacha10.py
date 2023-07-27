print("Введите n")
n = int(input())
orel = 0
gerb = 0
moneti = []
for i in range(n):
    print("Введите 1(орёл) или 0 (герб)")
    n = int(input())
    moneti.append(n)
    if n == 1:
        orel = orel + 1
    else:
        gerb = gerb + 1
print(*moneti)
if orel > gerb:
    print(f"Нужно перевернуть {gerb} монет")
else:
    print(f"Нужно перевернуть {orel} монет")