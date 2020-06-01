from itertools import combinations
j=1
count=0
lst=[]
ind=[]
le=int(input())
ls=list(map(str, input().split()))
for i in ls:
    if i == "a":
        ind.append(j)
        j=j+1
sep=int(input())
for i in range(1,le+1):
    lst.append(i)
total=len(list(combinations(lst,sep)))
for i in list(combinations(lst,sep)):
    if i[0] in ind:
        count = count+1
probablity=(count)/total        
print("%.4f" %probablity)