inp = int(input())

h = set(map(int, input().split()))
mx = max(h)
#print(mx)
rem = h.remove(mx)
print(max(h))
