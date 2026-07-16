def solution(slice, n):
    answer = 1
    while (answer * slice) / n < 1 :
        answer += 1
    return answer