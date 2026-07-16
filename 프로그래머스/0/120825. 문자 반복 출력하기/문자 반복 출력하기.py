def solution(my_string, n):
    answer = ''
    arr = []
    arr[:] = my_string
    for i in range(len(arr)) :
        for j in range(n) :
            answer += arr[i]
    
    return answer