
import sys
flag = 0
M = set()
N = set()
o = set()
while True:
    if flag >= 2:
        if flag == 4:
            break
        else:
            input_name2 = sys.stdin.readline()
            lst2 = input_name2.split()
            newlis2 = list(map(int, lst2))
            if flag == 2:
                flag = flag + 1
                continue

            N.update(newlis2)
            flag = flag + 1
    else:
        input_name1 = sys.stdin.readline()
        lst1 = input_name1.split()
        newlis1 = list(map(int, lst1))
        if flag == 0:
            flag = flag + 1
            continue
        M.update(newlis1)
        flag = flag + 1
#print(M)
#print(N)
o.update(M.difference(N)) 
o.update(N.difference(M))
s = sorted(o)
for sort in s:
    print(sort)
    
