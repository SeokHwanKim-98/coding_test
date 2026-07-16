def solution(n):
    answer = 0
    copy = str(n)
    copy_a = []
    copy_a[:] = copy
    copy_a.sort()
    copy_a.reverse()
    
    for i in range(len(copy_a)) :
        copy_a[i] = int(copy_a[i])
        print(f"{answer} * 10 + {copy_a[i]}")
        answer = answer * 10 + copy_a[i]
    return answer
