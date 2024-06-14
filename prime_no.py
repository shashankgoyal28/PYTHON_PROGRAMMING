flag = 0
n = int(input("input any no."))
i = 2
while (i <= n//2):
    if (n % i == 0):
        flag = 1
        break
    i += 1
if (flag == 0):
    print("prime no.")
else:
    print("not prime")
