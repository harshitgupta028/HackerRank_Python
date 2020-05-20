inp1, *inp2 = input().split()
inp1 = int(inp1)
inp2 = int(*inp2)
le = int((inp1-1)/2)

c=".|."

lw = int((inp2 - 3)/2) 

for i in range(1,le+1):
    print((c*i).rjust(lw+3,'-')+(c*(i-1)).ljust(lw,'-'))
print("WELCOME".center(inp2,'-'))

for i in reversed(range(1,le+1)):
    print((c*i).rjust(lw+3,'-')+(c*(i-1)).ljust(lw,'-'))
