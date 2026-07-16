def solution(my_string):
    answer = ''
    buff = []
    buff[:] = my_string
    buff.reverse()
    for i in range(len(buff)) :
        answer += buff[i]
    return answer