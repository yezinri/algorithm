T = int(input())
for i in range(T):
    N = int(input())
    result = []

    i = 0
    while N > 0:
        if N % 2:
            print(i, end=' ')
        N //= 2
        i += 1
    print()