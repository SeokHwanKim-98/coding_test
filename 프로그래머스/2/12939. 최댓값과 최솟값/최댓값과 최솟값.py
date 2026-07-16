def solution(s):
    answer = ''
    
    arr = s.split()
    for i in range(len(arr)) :
        arr[i] = int(arr[i])
    arr.sort()

    answer = f"{arr[0]} {arr[len(arr)-1]}"
    return answer