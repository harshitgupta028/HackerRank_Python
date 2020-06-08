import re
for i in range(int(input())):
    string=input()
    string=re.sub("(?<= )&&(?= )","and",string)
    string=re.sub("(?<= )\|\|(?= )","or",string)
    print(string)
