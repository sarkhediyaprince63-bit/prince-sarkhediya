def hourglass(N):
    if N % 2 == 0:
        print("enter a value")
        return

    for i in range (N, 0, -2):
        spaces = (N - i) //2
        print(" " *spaces + "*" * i)

    for i in range (3 , N + 1, 2):
        spaces = (N - i) //2
        print(" " *spaces + "*" * i)

hourglass(7)