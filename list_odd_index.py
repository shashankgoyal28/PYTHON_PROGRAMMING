# traversing a list.
a = [1, 2, 3, 4, 5, 6, 7]
sum = 0
for i in range(0, 7):
    if (i % 2 == 1):
        sum = sum+a[i]
print(sum)
