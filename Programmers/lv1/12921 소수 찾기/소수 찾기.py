def solution(n):
    prime = [1] * (n+1)
    
    for i in range(2, n+1):
        if prime[i] == 1:
            for j in range(i*2, n+1, i):
                prime[j] = 0
                
    return prime.count(1)-2
