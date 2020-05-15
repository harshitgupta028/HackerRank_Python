def count_substring(string, sub_string):
    c=0
    le = len(sub_string)
    for i in range(len(string)):
        if string[i:le+i] == sub_string:
            c = c + 1
        if le+i == len(string):
            break
    return(c)

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)