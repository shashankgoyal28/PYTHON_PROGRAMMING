t = tuple()
n = int(input("how many subjects you want to add"))
print("enter all subjects one after another")
for i in range(n):
    a = input("enter subject:")
    t += (a,)
print("output is")
print(t)
