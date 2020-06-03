import re
regex_pattern = r"([a-zA-Z0-9])\1+" #or r"(\w(?!_)\1+)" 
t = re.search(regex_pattern, input().strip())
if t == None:
    print("-1")
else:    
    print(t.group(1))