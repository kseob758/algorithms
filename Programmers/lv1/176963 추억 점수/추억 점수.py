def solution(name, yearning, photo):
    answer = []
    d = dict(zip(name, yearning))  # 두 리스트를 묶어 딕셔너리로
    for pt in photo:
        score = 0
        for p in pt:
            score += d.get(p, 0)
        answer.append(score)
    return answer
