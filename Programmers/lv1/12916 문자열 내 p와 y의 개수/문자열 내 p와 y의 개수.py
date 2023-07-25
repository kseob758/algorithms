def solution(s):
    s = s.lower()
    
    p_cnt, y_cnt = s.count('p'), s.count('y')
    
    return p_cnt==y_cnt

    
