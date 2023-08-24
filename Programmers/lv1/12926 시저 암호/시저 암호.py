def solution(s, n):
    lst = list(s) # 문자 하나씩 들어간 리스트
    answer = ''
    for a in lst:
        if a == ' ': # 문자가 공백이면 처리 없이 추가
            answer += a
        
        elif 65 <= ord(a) <= 90: # 소문자면
            new = ord(a)+n # 밀기
            if new > 90: # 소문자 코드 범위를 넘어가면
                new -= 26 # 순환으로 만들기
            answer += chr(new)
        elif 97 <= ord(a) <= 122: # 대문자면
            new = ord(a)+n # 밀기
            if new > 122: # 대문자 코드 범위를 넘어가면
                new -= 26 # 순환으로 만들기
            answer += chr(new)
    
    return answer
