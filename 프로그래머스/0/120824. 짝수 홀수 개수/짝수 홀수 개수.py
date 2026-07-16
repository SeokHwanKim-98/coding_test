def solution(num_list):
    answer = []
    count_e = 0
    count_o = 0
    
    for i in range(len(num_list)) :
        if num_list[i] % 2 == 0 :
            count_e += 1
        else :
            count_o += 1
    
    answer = [count_e,count_o]
    
    return answer