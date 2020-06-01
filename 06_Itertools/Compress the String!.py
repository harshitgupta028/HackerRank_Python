from itertools import groupby
ls=list(map(int, " ".join(input()).split(" ")))
for key, group in(groupby(ls)):
    print((len((list(group))), key),end=" ")