N = int(input())
arr = [0, 1]

for i in range(1, N):
    arr.append(arr[-2] + arr[-1])

print(arr[N])