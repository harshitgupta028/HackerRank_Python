import re
for i in range(int(input())):
    try:
        rex=re.compile(input())
        q="True"
    except re.error as e:
        q="False"
    print(q)
        
        