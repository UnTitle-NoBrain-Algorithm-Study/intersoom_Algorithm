import sys

ipt = sys.stdin.readline
userArr = []

for i in range(int(ipt())):
    userArr.append(int(ipt()))

userArr = sorted(userArr)

for i in userArr:
    print(i)
