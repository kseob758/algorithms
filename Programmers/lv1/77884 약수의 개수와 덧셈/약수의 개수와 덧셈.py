def solution(left, right):
    answer = 0
    
    while left<=right:  # left가 right보다 커지기 전까지
        cnt = 0
        for i in range(1,left+1):  # 1~left까지
            if left%i == 0:  # 약수 나오면 cnt 1증가
                cnt += 1
        if cnt%2==0:  # 약수 개수가 짝수면 +
            answer += left
        else:  # 홀수면 -
            answer -= left
        
        left += 1
        
    return answer
