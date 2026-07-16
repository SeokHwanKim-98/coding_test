def solution(n):
    copy = str(n)
    
    answer = []
    answer[:] = copy
    answer.reverse()
    for i in range(len(answer)):
        answer[i] = int(answer[i])
    return answer