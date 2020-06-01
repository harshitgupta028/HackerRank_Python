lis=[0,1]
cube = lambda x: x*x*x

def fibonacci(n):
    for i in range(0,n-2):
        lis.append(lis[i]+lis[i+1])
    if n==1:
        return([0])
    elif n==0:
        return([])
        
    return(lis)    


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))