def solution(arr):
    answer = []
    d = arr[0]
    for i in range(0,len(arr)) :
        # 배열 첫번째 값보다 크면 유지 작으면 변경
        if d < arr[i] :
            pass
            print(d)
        elif d > arr[i] :
            d = arr[i]
            print(d)
    arr.remove(d)

    if len(arr) > 0 :
        answer = arr
    else : answer = [-1]
    return answer