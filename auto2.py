list_1 = [1, 2, 3, 4, 5]
k = 6
nearest = int()
delta = 10000
for i in list_1:
    if  delta > abs(k - i):
        delta = abs(k - i)
        nearest = i
print(nearest)