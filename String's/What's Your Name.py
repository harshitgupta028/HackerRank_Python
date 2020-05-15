def print_full_name(a, b):
    print("Hello",end=" ")
    print(a,end=" ")
    print(b,end="")
    print("! You just delved into python.")
if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)