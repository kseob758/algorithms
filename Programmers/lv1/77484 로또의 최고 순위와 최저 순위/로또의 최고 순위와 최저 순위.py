def solution(lottos, win_nums):
    answer = []
    cnt = 0
    for num in lottos:
        if num in win_nums:
            cnt += 1
    max = cnt + lottos.count(0)
    
    for i in max, cnt:
        if i < 2:
            answer.append(6)
        else:
            answer.append(7-i)
            
    return answer
