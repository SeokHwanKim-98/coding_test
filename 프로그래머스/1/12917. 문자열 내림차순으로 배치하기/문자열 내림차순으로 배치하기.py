def solution(s):
    answer = ''
    arr = []

    arr[:] = s
    arr.sort()
    arr.reverse()

    for i in range (len(arr)) :
        answer += f"{(arr[i])}"    
        
    return answer