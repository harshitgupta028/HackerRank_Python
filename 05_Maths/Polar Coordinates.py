import cmath
inp=complex(input())

f=inp.real
s=inp.imag

z=complex(f,s)
for i in cmath.polar(z):
    print(i)
