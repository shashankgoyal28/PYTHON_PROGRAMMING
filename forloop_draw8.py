for rows in range(0, 7):
    for cols in range(0, 4):
        if (rows == 0 or rows == 3 or rows == 6 or cols == 0 or cols == 3):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
