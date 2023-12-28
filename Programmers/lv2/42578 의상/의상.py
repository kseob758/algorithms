def solution(clothes):
    d = {}
    answer = 1
    for c, k in clothes:
        d[k] = d.get(k, 0) + 1
    
    for v in d.values():
        answer *= (v+1)
        
    return answer-1
