def solution(numbers):
    answer = 0
    numbers.sort()
    
    for i in range(len(numbers)) :
        answer += numbers[i]
        
    answer = (45-answer)
    return answer