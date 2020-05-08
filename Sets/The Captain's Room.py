k = int(input())
arr =list(map(int ,input().split()))
inp1 = set(arr)
print(((sum(inp1)*k)-(sum(arr)))//(k-1))
