# program to store records of students in tuple
# and print them
st = ((200, "harmeet", 88),
      (201, "deepika", 98),
      (202, "harmeet", 78), (204, "harmeet", 90))
print("S_no", "roll_no", "name", "marks")
for i in range(0, len(st)):
    print((i+1), '\t', st[i][0], '\t', st[i][1], '\t', st[i][2])
