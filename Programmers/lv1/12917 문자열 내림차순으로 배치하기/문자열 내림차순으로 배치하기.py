def solution(s):
    reverse = sorted(s, reverse=True)
    answer = ''
    for i in reverse:
        answer += i
        
    return answer
