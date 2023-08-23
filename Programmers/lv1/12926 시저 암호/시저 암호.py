def solution(s, n):
    lst = list(s)
    answer = ''
    for a in lst:
        if a == ' ':
            answer += a
        
        elif 65 <= ord(a) <= 90:
            new = ord(a)+n
            if new > 90:
                new -= 26
            answer += chr(new)
        elif 97 <= ord(a) <= 122:
            new = ord(a)+n # 밀기
            if new > 122:
                new -= 26
            answer += chr(new)
    
    return answer
