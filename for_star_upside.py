for i in range(1, 5):
    if (i > 1):
        for k in range(1, i):
            print(" ", end=" ")
    for j in range(5, i, -1):
        print("*", end=" ")
    print()
