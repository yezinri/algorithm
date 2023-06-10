maxN, nowN = 0, 0
for i in range(10):
    off, on = map(int, input().split())
    nowN += (on - off)
    if nowN > maxN:
        maxN = nowN

print(maxN)