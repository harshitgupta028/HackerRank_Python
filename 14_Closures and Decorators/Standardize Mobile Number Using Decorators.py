# Using decorators
 
def wrapper(f):
    def fun(l):
        f(["+91 "+c[-10:-5]+" "+c[-5:] for c in l])
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 

# using closures
def sort(lis):
    mob_lis=sorted(lis)
    def formated():
        for i in mob_lis:
            print("+91",i[:5],i[5:])
    return(formated)     
mob=[]
for _ in range(int(input())):
    i=input()
    if len(i)!=10:
        if i.startswith("0"):
            mob.append(i.replace("0","",1))
        if i.startswith("91"):
            mob.append(i.replace("91","",1))
        if i.startswith("+91"):
            mob.append(i.replace("+91","",1))
    else:
        mob.append(i)
mob_no=sort(mob)        
mob_no()

     
