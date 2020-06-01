inp =int(input())

for i in range(inp):
    l1 = int(input())
    s1 = list(map(int, input().split()))
    
    #if s1[0] >= s1[-1]:
    if max(s1) in (s1[0],s1[-1]):
        print("Yes")
    else:
        print("No")
