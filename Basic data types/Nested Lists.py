student = list()
ans = list()
for _ in range(int(input())):
    name = input()
    score = float(input())
    student.append([score, name])

student=sorted(student)    
mn=student[0][0]

i=0
for check in student:
    if check[0] == mn:
        i+=1
    else:
        break;
        
mn=student[i][0]

for ch in range(i,len(student)):
    if student[ch][0] == mn:
        ans.append(student[ch][1])
    else:
        break
for i in sorted(ans):
    print(i)
