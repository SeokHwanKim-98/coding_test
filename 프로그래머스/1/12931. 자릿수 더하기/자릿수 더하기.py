def solution(n):
    arr = []
    answer = 0
    copy = str(n)
    arr[:] = copy

    for i in range (len(arr)) :
        arr[i] = int(arr[i])
        answer += arr[i]
        

    return answer