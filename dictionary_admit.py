SCL = dict()
i = 1
flag = 0
n = int(input("enter number of entries:"))
while i <= n:
    Adm = input("\n enter admission no of a student:")
    nm = input("enter name of the student:")
    section = input("enter class and section:")
    per = float(input("enter the percentage of a student:"))
    b = (nm, section, per)
    SCL[Adm] = b
    i = i+1
l = SCL.keys()
for i in l:
    print("\nAdmno-", i, " :")
    Z = SCL[i]
    print("Name\t", "class\t", "per\t")
    for j in z:
        print(j, end="\t")
