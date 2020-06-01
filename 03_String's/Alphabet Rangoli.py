import string
st = string.ascii_lowercase
lst = list()
def print_rangoli(size):
    for i in range(size):
        s="-".join(st[i:size])
        lst.append((s[::-1]+s[1:]).center(4*size-3,"-"))
    print("\n".join(lst[::-1]+lst[1:]))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)