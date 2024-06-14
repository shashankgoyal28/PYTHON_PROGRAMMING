# print a seprate list for even and odd no. from a given list
list1 = [1, 2, 3, 4, 5, 6]
even = 0
odd = 0
list_even = []
list_odd = []
len1 = len(list1)
for i in list1:
    if (i % 2 != 0):
        list_odd.append(i)
        odd += 1
    else:
        list_even.append(i)
        even += 1
print(list_even)
print(list_odd)
print(odd)
print(even)
