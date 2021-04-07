print("\n")

for y in range(1, 11):
    for x in range(1, 11):
        if y == 1 or y == 10:
            print("# ", end="")
        elif x > 1 and x < 10:
                print('. ', end="")
        else:
            print("# ", end="")
    print()

print("\n")
