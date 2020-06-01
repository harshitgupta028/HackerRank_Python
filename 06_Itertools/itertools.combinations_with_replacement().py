from itertools import combinations_with_replacement
st,*r = input().split()
for j in list(combinations_with_replacement(sorted(st),int(r[0]))):
    print(*j,sep="")


# these are the more ways to find permutations

#>>> from itertools import combinations_with_replacement
#>>> 
#>>> print list(combinations_with_replacement('12345',2))
#[('1', '1'), ('1', '2'), ('1', '3'), ('1', '4'), ('1', '5'), ('2', '2'), ('2', '3'), ('2', '4'), ('2', '5'), ('3', '3'), ('3', '4'), ('3', '5'), ('4', '4'), ('4', '5'), ('5', '5')]
#>>> 
#>>> A = [1,1,3,3,3]
#>>> print list(combinations(A,2))
#[(1, 1), (1, 3), (1, 3), (1, 3), (1, 3), (1, 3), (1, 3), (3, 3), (3, 3), (3, 3)]