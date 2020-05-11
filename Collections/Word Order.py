dic = dict()
for _ in range(int(input())):
    inp = input()
    dic[inp] = dic.get(inp,0)+1

#print(dic)
print(len(dic))

for k,v in dic.items():
    print(v,end=' ')

