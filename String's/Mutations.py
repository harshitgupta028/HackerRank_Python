def mutate_string(string, position, character):
    st = list(string)
    st[position] = character
    return("".join(st))


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)