for rows in range(1, 8):
    for cols in range(1, 8):
        if ((cols == 1 and cols == 8) or rows == 4):
            print("*", end=" ")
        elif ((cols == 2 and cols == 7) or rows == 3):
            print("*", end=" ")
        elif ((cols == 3 and cols == 6) or rows == 2):
            print("*", end=" ")
        elif ((cols == 4 and cols == 5) or rows == 1):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
