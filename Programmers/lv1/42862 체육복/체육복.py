def solution(n, lost, reserve):
    dic = {}
    for i in range(1,n+1):
        dic[i] = 1
    
    for j in lost:
        dic[j] -= 1
    
    for k in reserve:
        dic[k] += 1
        
    for l in dic:
        if dic[l] > 1:
            if l > 1 and l < n:
                if dic[l-1]==0:
                    dic[l] -= 1
                    dic[l-1] += 1
                elif dic[l+1]==0:
                    dic[l] -= 1
                    dic[l+1] += 1
            elif l == 1 and dic[l+1]==0:
                dic[l] -= 1
                dic[l+1] += 1
            elif l==n and dic[n-1] == 0:
                dic[l] -= 1
                dic[l-1] += 1

    answer = [s for s in dic if dic[s] > 0]

    return len(answer)
