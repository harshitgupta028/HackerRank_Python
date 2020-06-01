#SOLLUTION

n = int(input())
s = set(map(int, input().split()))
n = int(input())
for t in range(n):
    
    i = input().split()
    #print(i)
    
    try:
        if i[0] == 'pop':
            q = i[0]
        else:
            q = i[0]
            k = i[1]
            k=int(k)
    except:
        None
        
    if q == 'pop':
        s.pop()
    elif q == 'remove':
        s.remove(k)
    elif q == 'discard':
        s.discard(k) 
if len(s) is 0:
    print("0") 
else:
    print(sum(s))
