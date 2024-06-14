for i in range(0, 5):
    for j in range(4, i, -1):
        print(" ", end=" ")
    for k in range(0, i):
        print("  *", end=" ")
    print()
