def solution(my_string, letter):
    answer = ''
    arr = []
    arr[:] = my_string


    while letter in arr:
        arr.remove(letter)
        
    for i in range(len(arr)) :
        answer += arr[i]
        
    return answer