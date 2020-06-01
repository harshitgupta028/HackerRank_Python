i,lis=int(input()), list(input().split())
print(all(int(i) >= 0 for i in lis) and any(j == j[::-1] for j in lis))

   
        