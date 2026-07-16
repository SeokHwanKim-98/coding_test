def solution(sizes):
    answer = 0
    buff = 0
    max_a = 0
    max_b = 0

    ##이중배열 정렬
    for i in range(len(sizes)) :
        if sizes[i][0] > sizes[i][1] :
            buff = sizes[i][0]
            sizes[i][0] = sizes[i][1]
            sizes[i][1] = buff

        if max_a < sizes[i][0]:
            max_a = sizes[i][0]

        if max_b < sizes[i][1]:
            max_b = sizes[i][1]

    
    answer = max_a * max_b

    return answer