def solution(n):
    arr = []
    answer = 0
    copy = str(n)
    arr[:] = copy

    arr = [int(i) for i in arr]

    for i in range(len(arr)) :
        answer += arr[i]

    return answer