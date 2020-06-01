X = int(input())

Y = int(input())

Z = int(input())

n = int(input())

lst = list()

for i in range(X + 1):
    for j in range(Y + 1):
        for k in range(Z + 1):
            if (i+j+k) != n:
                lst.append([i,j,k])
print(lst)

