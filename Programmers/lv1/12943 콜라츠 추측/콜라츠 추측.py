def solution(num):
    answer = 0
    if num == 1: # 1 입력시 0 반환
        return 0
    
    while num != 1: # 1이 될 때까지
        if num%2 == 0: # 짝수일 경우
            num //= 2
        else: # 홀수일 경우
            num = num*3 + 1
        answer += 1 # 작업 횟수 +1
        
        if answer == 500: # 500회까지 1이 되지 않으면
            return -1
        
    return answer
