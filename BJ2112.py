from sys import stdin

sum = 0

N = int(stdin.readline())

rankList = [0] * N
sortedRankList = [0] * N

for i in range(N):
	rankList[i] = int(stdin.readline())

sortedRankList = sorted(rankList)

for index, value in enumerate(sortedRankList):
    sum += abs(value - (index + 1))

print(sum)