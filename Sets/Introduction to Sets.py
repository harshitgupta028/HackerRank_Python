def average(array):
    se = set(array)
    length = len(se)
    return(sum(se)/length)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)