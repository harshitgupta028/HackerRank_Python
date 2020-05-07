student = dict()

inp = int(input())
for i in range(inp):
    
    l2 = input().split()
    name = l2[0]
    l2.remove(name)
    #print(l2)
    l3 = list(map(float, l2))
    score = sum(l3)/3
    #print(score)
    student[name] = score
l4 = input()
print('%.2f'%student[l4])
    