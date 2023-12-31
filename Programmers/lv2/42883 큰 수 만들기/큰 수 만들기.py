def solution(number, k):
    collected = []
    
    for i, num in enumerate(number):
        while len(collected) > 0 and collected[-1] < num and k > 0:
            collected.pop()
            k -= 1
        
        if k == 0:
            collected += list(number[i:])
            break
            
        collected.append(num)
    
    if k > 0:
        collected = collected[:-k]
    
    answer = ''.join(collected)
        
    return answer
