import re
for i in range(int(input())):
    mob=input()
    if len(mob) == 10:
        if re.match(r"^[789]\d+$",mob):
            print("YES")
        else:
            print("NO")
    else:    
        print("NO")