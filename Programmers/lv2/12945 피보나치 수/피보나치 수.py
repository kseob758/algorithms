def solution(n):
    f = [0, 1]
    
    for i in range(2, n+1):
        f.append(f[i-2] + f[i-1])
                            
    result = f[-1] % 1234567 
    
    return result
