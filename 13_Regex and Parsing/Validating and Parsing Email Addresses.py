import re 
for i in range(int(input())):
    email=input()
    che=re.search(r"[A-Za-z]+ <[a-z0-9]+[a-z\._-]*[a-z0-9]+[@][a-z]+[.][a-z]{1,3}>$",email)
    if che:
        print(che.group())
    