# delete all odd numbers and negative numbers
list1 = [11, -1, 22, -3, 33, 55, 44, -50, 46, 101, 77, -100, 42]
len1 = len(list1)
i = 0
while i < len1:
    if (list1[i] < 0):
        del list1[i]
        len1 = len1 - 1
        i = i-1
    elif (list1[i] % 2 != 0):
        del list1[i]
        len1 = len1 - 1
        i = i - 1
# what is this i = i+1 here used for ?
    i = i+1
print("list after deletions:", list1)
