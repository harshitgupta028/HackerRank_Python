import re
for i in range(int(input())):
    credit_no=input()
    if len(credit_no)==16 or 19:
        if "-" in credit_no:
            if re.findall(r"^[456]\d{3}-\d{4}-\d{4}-\d{4}$",credit_no):
                credit_no=credit_no.replace("-","")
            
        if len(credit_no)==16:
            if re.findall(r"^[456]\d+$",credit_no) and len(re.findall(r"(.)\1{3,}",credit_no))==0:
                print("Valid")
            else:
                print("Invalid")
        else:
            print("Invalid")
    else:
        print("Invalid")

# IGNORE THIS PART

#import re
#print(re.findall(r"^[456]\d{3}-\d{4}-\d{4}-\d{4}$","5122-2368-7954-3214"))
#s="5122-24687954-3214"
#if "-"in s:
#    sn=s.replace("-","",3)
#    print(sn)
#print(re.findall(r"(.)\1{4}",sn))

#import re
#a="aaabbjaajjjc"
#print(re.findall(r"(.)\1{4}",a))
#st="harshit"
#st="gupta"
#print(st)
