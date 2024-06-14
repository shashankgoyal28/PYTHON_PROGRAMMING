for rows in range(1, 8):
    for cols in range(1, 8):
        if (rows == cols) or (rows == 8 - cols):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
