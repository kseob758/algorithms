def solution(n, arr1, arr2):
    answer = [''] * n
    
    for i in range(len(arr1)):
        arr1[i] = bin(arr1[i])[2:].zfill(n)
        arr2[i] = bin(arr2[i])[2:].zfill(n)
        
    index = 0
    
    for a,b in zip(arr1,arr2):
        for i in range(n):
            answer[index] += '#' if int(a[i])|int(b[i])==1 else ' '
        index += 1
        
    return answer
