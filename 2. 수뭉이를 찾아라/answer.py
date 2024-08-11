def ans(i, str):
    cnt = 0

    for i in range(0,len(str), 2):
        if(str[i] == 'S' and str[i+1] == 'M'):
            cnt+=1
    
    return cnt
