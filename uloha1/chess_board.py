size = int(input())


for i in range(size):
    for j in range(size):
        if i % 2 == 0:
            j += 1

        if j % 2 == 0:
            print("*", end = "")
        else:
            print("O", end = "")

    print(" ")