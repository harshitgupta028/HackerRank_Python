/*
Task:
Given  sets of integers,  and , print their symmetric difference in ascending order. The term symmetric difference indicates those values that exist in either  or  but do not exist in both.

Input Format:

The first line of input contains an integer, .
The second line contains  space-separated integers.
The third line contains an integer, .
The fourth line contains  space-separated integers.

Output Format:

Output the symmetric difference integers in ascending order, one per line.

Sample Input:

4
2 4 5 9
4
2 4 11 12

Sample Output:

5
9
11
12
*/

========================================================================================================================================================================
Sollution:
========================================================================================================================================================================

import sys
flag = 0
M = set()
N = set()
o = set()
while True:
    if flag >= 2:
        if flag == 4:
            break
        else:
            input_name2 = sys.stdin.readline()
            lst2 = input_name2.split()
            newlis2 = list(map(int, lst2))
            if flag == 2:
                flag = flag + 1
                continue

            N.update(newlis2)
            flag = flag + 1
    else:
        input_name1 = sys.stdin.readline()
        lst1 = input_name1.split()
        newlis1 = list(map(int, lst1))
        if flag == 0:
            flag = flag + 1
            continue
        M.update(newlis1)
        flag = flag + 1
#print(M)
#print(N)
o.update(M.difference(N)) 
o.update(N.difference(M))
s = sorted(o)
for sort in s:
    print(sort)
    