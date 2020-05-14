def minion_game(string):
    k_score = 0
    s_score = 0
    vow = 'AEIOU' 

    for check in range(len(string)):

        if string[check] in vow:
            k_score = k_score + len(string)-check
        else:
            s_score = s_score + len(string)-check
 
    if k_score > s_score:
        print ("Kevin", k_score)
    elif k_score < s_score:
        print ("Stuart", s_score)
    else:
        print ("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)