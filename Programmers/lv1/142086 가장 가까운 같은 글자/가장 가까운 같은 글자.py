def solution(s):
    answer = []
    for idx, i in enumerate(s):
        tmp = s[:idx][::-1].find(i)
        if tmp != -1:
            tmp += 1
        answer.append(tmp)
            
    return answer
