a = int(input("enter the no."))
sum = 0
while (a > 0):
    r = a % 10
    sum = sum*10 + r
    a = a//10
print(sum)
