def solution(s):
    answer = ''
    arr = []
    arr[:] = s
    mid = len(arr) // 2
    
    if len(arr) % 2 == 0 :
        answer = f"{arr[mid-1]}{arr[mid]}"
    else :
        answer = arr[mid]
    return answer