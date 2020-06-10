import re 
for i in  range(int(input())):
    try:
        c=input()
        if len(c)==0:
            continue
        while True:
            color=input()
            if color!="}":
                che=re.findall(r"(#[0-9a-fA-F]{6}|#[0-9a-fA-F]{3})",color)
                for i in che:
                    if len(i)>0:
                        print(i)
            else:
                break
    except EOFError:
        None
    