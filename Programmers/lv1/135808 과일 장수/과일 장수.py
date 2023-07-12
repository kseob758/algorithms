def solution(k, m, score):
    answer = 0
    apples = sorted(score, reverse=True)
    for i in range(len(score) // m):  # 상자 개수 : len(score) // m
        answer += min(apples[i*m:i*m+m]) * m
    return answer
