t1 = tuple()
n = int(input("total no of values in first tuple:"))
for i in range(n):
    a = input("enter elements:")
    t1 = t1+(a,)
    t2 = tuple()
m = int(input("total no.of values in second tuple:"))
for i in range(m):
    a = input("enter elements:")
    t2 = t2+(a,)
print("first tuple:")
print(t1)
print("second tuple:")
print(t2)
t1, t2 = t2, t1
print("after swapping:")
print("first tuple:")
print(t1)
print("second tuple:")
print(t2)
