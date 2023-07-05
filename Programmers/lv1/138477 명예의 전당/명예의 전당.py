def solution(k, score):
    fame = []
    answer = []
    for i in score:
        fame.append(i)
        if len(fame) > k:
            fame.remove(min(fame))
        answer.append(min(fame))
    return answer
