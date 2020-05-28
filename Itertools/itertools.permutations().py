from itertools import permutations
st,*r = input().split()
for i in list(sorted(permutations(st,int(r[0])))): 
    print(*i,sep="")


# these are the more ways to find permutations

#>>> from itertools import permutations
#>>> print permutations(['1','2','3'])
#<itertools.permutations object at 0x02A45210>
#>>> 
#>>> print list(permutations(['1','2','3']))
#[('1', '2', '3'), ('1', '3', '2'), ('2', '1', '3'), ('2', '3', '1'), ('3', '1', '2'), ('3', '2', '1')]
#>>> 
#>>> print list(permutations(['1','2','3'],2))
#[('1', '2'), ('1', '3'), ('2', '1'), ('2', '3'), ('3', '1'), ('3', '2')]
#>>>
#>>> print list(permutations('abc',3))
#[('a', 'b', 'c'), ('a', 'c', 'b'), ('b', 'a', 'c'), ('b', 'c', 'a'), ('c', 'a', 'b'), ('c', 'b', 'a')]



#we can also chang our for loop like: for i in list(permutations(sorted(st),int(r[0]))):
