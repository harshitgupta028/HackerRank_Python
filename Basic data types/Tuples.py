inp = input()

inp2 = tuple(map(int, input().split()))
print(hash(inp2))

#                              Properties of hash()
#     * Objects hashed using hash() are irreversible, leading to loss of information.
#     * hash() returns hashed value only for immutable objects, hence can be used as an 
#       indicator to check for mutable/immutable objects.
