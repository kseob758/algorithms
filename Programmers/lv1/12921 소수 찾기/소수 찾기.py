# 에라토스테네스의 체

def solution(n):
    prime = [1] * (n+1)  # index 0~n
    
    for i in range(2, n+1):  # 2부터 n까지
        if prime[i] == 1:  # prime[i]가 1이면 (소수이면)
            for j in range(i*2, n+1, i):  # i의 배수인 i*2부터 i*3, i*4, ... <=n 까지
                prime[j] = 0  # 소수가 아닌 것으로 판명
                
    return prime.count(1)-2  #초기화 할 때 들어간 index 0,1 빼주기
