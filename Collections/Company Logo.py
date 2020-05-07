from collections import Counter

inp = sorted(input())

counter = Counter(inp)

for ok in counter.most_common(3):
    print(*ok)



