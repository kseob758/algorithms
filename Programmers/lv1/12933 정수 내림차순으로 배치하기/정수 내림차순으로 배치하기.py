def solution(n):
    lst = sorted(list(str(n)), reverse=True)
    
    answer = ''
    for num in lst:
        answer += str(num)
        
    return int(answer)
