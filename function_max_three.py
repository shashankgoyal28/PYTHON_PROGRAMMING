# Find the maximum of three numbers.
# This function should take three numbers
# as input and
# return the largest of the three.
def maximum_number(n1, n2, n3):
    if (n1 > n2) and (n1 > n3):
        print(n1)
    elif (n2 > n3) and (n2 > n1):
        print(n2)
    elif (n3 > n2) and (n3 > n1):
        print(n3)


x = int(input("enter the 1st no."))
y = int(input("enter the 2nd no."))
z = int(input("enter the 3rd no."))
maximum_number(x, y, z)
