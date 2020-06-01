a,b=map(int, input().split())
lis=[]
for i in range(b):
    lis.append(map(float, input().split()))
for i in zip(*lis):
    print(sum(i)/len(i))