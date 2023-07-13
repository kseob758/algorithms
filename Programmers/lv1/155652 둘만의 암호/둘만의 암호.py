def solution(s, skip, index):
    answer = ""
    alpha = "abcdefghijklmnopqrstuvwxyz"  # 알파벳 a~z
    
    for ch in skip:
        alpha = alpha.replace(ch, "")  # 알파벳 안에 skip 문자들 제거
    
    for i in s:
        change = alpha[(alpha.index(i) + index) % len(alpha)]  # index만큼 뒤의 알파벳(z를 넘으면 다시 앞으로)
        answer += change
    
    return answer
