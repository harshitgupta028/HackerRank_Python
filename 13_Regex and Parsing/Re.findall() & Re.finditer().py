import re
v="aeiou"
c="qwrtypsdfghjklzxcvbnm"
lis=re.findall(r"(?<=[%s])([%s]{2,})[%s]"%(c,v,c),input().strip() , flags=re.IGNORECASE)
print(-1) if len(lis)==0 else print("\n".join(lis))


