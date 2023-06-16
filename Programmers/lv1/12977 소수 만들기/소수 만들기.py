from itertools import combinations

def is_prime(x):
    for i in range(2,x):
        if x%i == 0:
            return False
    return True

def solution(nums):
    cnt = 0
    combi = list(combinations(nums, 3))
    
    for data in combi:
        if is_prime(sum(data)):
            cnt += 1

    return cnt
