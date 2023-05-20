def solution(N, stages):
    answer = []
    dic, fail = {}, {}

    for i in range(1,N+1): # 도달한 유저가 없는 경우 0으로 하기 위해 dictionary를 0으로 초기화
        dic[i], fail[i] = 0, 0
    
    for stage in stages: # dic은 도달한 유저 수 fail은 실패한 유저 수
        if stage > N: #끝까지 클리어 한 경우 끝까지 도달
            dic[N] += 1
        else: # 도달, 실패 둘 다 1씩 증가
            dic[stage] += 1
            fail[stage] += 1
            
    for d in dic: #스테이지 1부터 도달한 누적 유저 수 추가해주기
        s = 1
        while s < d:
            dic[s] += dic[d]
            s += 1
    
    for j,k in zip(dic, fail):
        if dic[j] != 0:
            fail[k] /= dic[j] # 도달한 사람이 0이 아니면 나누어서 갱신. divide by zero 방지
    
    answer = sorted(fail, key = fail.get, reverse = True) # value기준 내림차순 정렬 리스트
    return answer
