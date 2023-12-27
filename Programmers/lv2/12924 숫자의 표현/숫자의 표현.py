def solution(n):
    if n == 1:
        return 1
    result = 0 if n % 2 == 0 else 1
    for i in range(1, n//2):
        total = 0
        for j in range(i, n//2):
            total += j
            if total == n:
                result += 1
                break
            if total > n:
                break
    return result+1
