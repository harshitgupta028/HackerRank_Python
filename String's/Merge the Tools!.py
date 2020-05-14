def merge_the_tools(string, k):
   
    length = len(string)
    s = int(length/k)
    p = 0
    ilt = k
    for str in range(s):  
        t = string[p:ilt]
    
        lst = list()

        for ch in t:
            if ch not in lst:
                lst.append(ch)
                print(ch,sep=' ',end='')
        print('\n',end='')        
        p = ilt
        ilt = ilt + k
        
 if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
