def solution(x):
    total = 0
    num = x
    while num>0:
        total += num%10
        num //= 10
    
    return x%total == 0
