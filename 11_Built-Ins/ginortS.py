inp=input()
order = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1357902468'
for i in sorted(inp, key=order.index):
    print(i,end="")

