from sys import stdin
from collections import Counter

N = int(stdin.readline())

numList = [0] * N
userAvg = 0
userMid = 0
userFrq = 0
userRange = 0

for i in range(N):
	numList[i] = int(stdin.readline())

userLen = len(numList)

numList.sort()

for i in numList:
    userAvg += i

userAvg = round(userAvg / userLen)

userMid = sorted(numList)[userLen // 2]

repeat = Counter(numList).most_common()

if len(repeat) == 1:
    userFrq = repeat[0][0]
elif repeat[0][1] == repeat[1][1]:
    userFrq = repeat[1][0]
else:
    userFrq = repeat[0][0]


userRange = max(numList) - min(numList)

print(userAvg)
print(userMid)
print(userFrq)
print(userRange)








