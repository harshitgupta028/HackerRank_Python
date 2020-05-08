#inp_1 = int(input())
s_list = list()
index = 0
for i in range(int(input())):
    if i == 0:
        header = list(map(str, input().split()))
        for i in header:
            if i == ("MARKS"):
                break
            index = index+1
    marks = list(map(str, input().split()))
    s_list.append(marks[index])
    m_list = list(map(int, s_list))
avg = (sum(m_list))/(len(m_list))    
print('%.2f'%avg)

#========================================================================================================================
#ALTERNATE
#=========================================================================================================================

from collections import namedtuple
N = int(input())

student = namedtuple('student',input().strip().split())

print(sum(float(student(*input().strip().split()).MARKS) for _ in range(N))/N)

    
    
    
