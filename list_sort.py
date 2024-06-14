list1 = [32, 24, 56, 76, 19]
i = 0
len1 = len(list1)
print(len1)
while i < len1:
    j = i+1
    while (j < len1):
        if (list1[i] > list1[j]):
            list1[i], list1[j] = list1[j], list1[i]
        j += 1
    i += 1
print(list1)
print(list1[-2])
