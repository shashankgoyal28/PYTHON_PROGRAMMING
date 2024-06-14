def print_star_pattern(n):
    for i in range(n):
        for j in range(n - i):
            print("  ", end=" ")
        for k in range(i):
            print("  *", end=" ")
        print()


if __name__ == "__main__":
    print_star_pattern(4)
