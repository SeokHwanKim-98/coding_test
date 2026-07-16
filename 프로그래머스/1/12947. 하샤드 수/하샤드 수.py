def solution(x):
    answer = True
    temp = 0
    sol = 0
    x1 = x

    while (x1 / 10) > 0 :
        temp = x1 % 10
        sol += temp
        x1 = x1 // 10    

    if x % sol == 0 :
        answer = True

    else : answer = False

        
    return answer