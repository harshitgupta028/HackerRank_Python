from collections import OrderedDict
dic = OrderedDict()
for _ in range(int(input())):
    item, space, quantity = input().rpartition(' ')
    dic[item] = dic.get(item, 0) + int(quantity)
for i in dic.items():
    print(*i)
    
# .rpartition() function in Python split the given string into three parts. 
#  rpartition() start looking for separator from right side, till the separator 
#  is found and return a tuple which contains part of the string before separator, 
#  argument of the string and the part after the separator.
