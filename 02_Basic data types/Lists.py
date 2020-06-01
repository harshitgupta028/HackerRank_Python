lis  = list()

for _ in range(int(input())):
    
    perf,*values = input().strip().split()
    values = list(map(int, values))
    if perf == 'insert':
        index = values[0]
        val = values[1]
        lis.insert(index,val)
    elif perf == "print":
        print(lis)
    elif perf == "append":
        lis.append(values[0])
    elif perf == "remove":
        lis.remove(values[0])
    elif perf == "sort":
        lis.sort()
    elif perf == "pop":
        lis.pop()
    elif perf == "reverse":
        lis.reverse()
        
        
