from sys import stdin

N = int(stdin.readline())

userList = [0] * N
resultList = [0] * N
stack = []

for i in range(N):
    userList[i] = stdin.readline()

for i in range(N):
    stack = []
    for j in range(len(userList[i])):
        test = userList[i][j]
        if test == '(':
            stack.append(test)
        elif test == ')':
            if '(' in stack:
                stack.pop()
            else:
                stack.append(')')
    if len(stack) == 0:
        print("YES")
    else:
        print("NO")
