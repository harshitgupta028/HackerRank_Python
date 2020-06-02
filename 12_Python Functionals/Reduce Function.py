from fractions import Fraction
from functools import reduce

def product(fracs):
    F1=reduce(lambda x,y: x*y, fracs)
    
    return F1.numerator, F1.denominator

if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)