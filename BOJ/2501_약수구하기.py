N, K = map(int, input().split())
resultList = []

for i in range(1, N+1):
    if N % i == 0:
        if i in resultList:
            break
        else:
            resultList.append(i)
            if N//i not in resultList:
                resultList.append(N//i)

if len(resultList) >= K:
    print(sorted(resultList)[K-1])
else:
    print(0)