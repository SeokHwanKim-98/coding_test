def solution(a, b):
    answer = 0
    
    if a < b :
        for i in range(a,b+1) :
            if i <= b :
                answer += i
    else :
        for i in range(b,a+1) :
            if i <= a :
                answer += i
    
    return answer