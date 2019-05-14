a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = []
for i in a:
    if (i**3) % 3 == 1:
        b.append(i)
print(b)
