N = int(input())
arr = list(map(int,input().split()))

minN, maxN = arr[0], arr[0]
for n in arr:
    if n > maxN:
        maxN = n
    elif n < minN:
        minN = n

print(minN, maxN)