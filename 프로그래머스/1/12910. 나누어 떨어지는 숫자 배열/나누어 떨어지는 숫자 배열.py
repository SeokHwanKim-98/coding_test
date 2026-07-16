def solution(arr, divisor):
    answer = []
    d_arr = []
    
    for i in range(len(arr)) :
        if arr[i] % divisor == 0 :
            pass
        else : d_arr.append(arr[i])
    

    for j in range(len(d_arr)) :
        arr.remove(d_arr[j])

    arr.sort()    
    if len(arr) > 0 :
        answer = arr
    else : answer = [-1]
        
    
    return answer