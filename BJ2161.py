# 버리고 -> 옮기고
N = int(input())
card = list(range(N, 0, -1))
result = []

while len(card) != 0:
    result.append(card.pop())

    if len(card) > 0:
        card.insert(0, card[-1])
        del card[-1]

for i in result:
    print(i, "", end='')
