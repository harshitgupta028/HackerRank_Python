from collections import Counter

inp  = input()
inp2 = Counter(list(map(int, input().split())))
c=list(inp2.elements())
sm  = 0
inp3 = int(input())
for l in range(inp3):
    inp4,*price = input().split()
    #print(price)
    inp4 = int(inp4)
    price = int(*price)
    if inp4 in c:
        c.remove(inp4)
        sm = sm + price
print(sm)