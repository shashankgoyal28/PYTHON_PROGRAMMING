# Sum all the numbers in a list.This function should take
# a list of numbers as input and return the sum of all the numbers in the list.
def sum_list(list3):
    sum = 0
    for i in range(0, len(list3)):
        sum = sum + list3[i]
    print(sum, end=" ")


list2 = []
n = int(input("enter the no. of elements: "))
for i in range(0, n):
    a = int(input())
    list2.append(a)
sum_list(list2)
