from sys import stdin
from collections import deque

N, K = stdin.readline().split(" ")

N = int(N)
K = int(K)

peopleList = [0] * N
killList = [0] * N

for i in range(N):
    peopleList[i] = i + 1

i = 0

deque = deque(peopleList)

while len(deque) != 0:
    deque.rotate(-K)
    killList[i] = str(deque.pop())
    i += 1



resultStr = "<"
resultStr += ", ".join(killList)
resultStr += ">"

print(resultStr)