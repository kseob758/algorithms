def solution(participant, completion):
    dic = {}
    for par in participant:
        dic[par] = dic.get(par,0) + 1  # get 메소드 : 첫번째 인자를 키로 하는 값을 반환. 없으면 두번째 인자 반환
        
    for com in completion:
        dic[com] -= 1
    
    for i in dic:
        if dic[i] == 1:
            return i
