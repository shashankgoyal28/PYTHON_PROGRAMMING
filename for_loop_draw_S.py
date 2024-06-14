for rows in range(1, 8):
    for cols in range(1, 5):
        if (rows == 1 or rows == 4 or rows == 7):
            print("*", end=" ")
        elif ((rows == 2 or rows == 3) and cols == 1):
            print("*", end=" ")
        elif ((rows == 5 or rows == 6) and cols == 4):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
