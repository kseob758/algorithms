def solution(d, budget):
    answer = 0
    d.sort() # 부서별 신청 금액 오름차순 정렬

    if sum(d) <= budget: # 신청 금액 총합이 예산으로 커버 되면
        return len(d) # 부서 개수 리턴
    
    while d[0] <= budget:   # 제일 낮은 금액이 예산보다 작을 때까지
        budget -= d.pop(0)  # 그 금액 지우면서 예산에서 차감
        answer += 1 # 지원 부서 수 +1

    return answer
