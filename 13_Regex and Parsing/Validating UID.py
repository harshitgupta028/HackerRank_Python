import re
for i in range(int(input())):
    uids="".join(sorted(input()))
    if len(uids)==10:
        if len(re.findall(r"(.)\1*",uids))==10 and re.findall(r"[a-zA-Z0-9]",uids) and re.findall(r"[0-9]{3,}",uids) and re.findall(r"[A-Z]{2,}",uids):
            print("Valid")
        else:
            print("Invalid")
    else:
        print("Invalid")
        
        
        
#   a="aaaabbjjjjc"
#   print(re.findall(r"(.)\1*",a))

#   OUTPUT:
#   ['a', 'b', 'j', 'c']