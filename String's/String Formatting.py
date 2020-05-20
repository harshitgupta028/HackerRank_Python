def print_formatted(number):
    
    w=len(bin(number)[2:])
    for i in range(1,number+1):
        
        print(str(i).rjust(w," "), end=" ")
        o = oct(i)
        print(o[2:].rjust(w," "), end=" ")
        h = hex(i)
        if h[2:] == 'a'or'b'or'c'or'd'or'e'or'f':
            print(h[2:].upper().rjust(w," "), end=" ")
        else:    
            print(h[2:].rjust(w," "), end=" ")
        b = bin(i)
        print(b[2:].rjust(w," "),end=" ")
        print("")
        i+=1
    

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)