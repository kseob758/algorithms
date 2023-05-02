def solution(s):
    yes, no = 0, 0
    first = ''
    answer = 0
    
    for c in s:
        if first == '':
            first = c
            yes += 1
            continue
        if c == first:
            yes += 1
        else:
            no += 1
        
        if yes == no:
            answer += 1
            yes, no = 0, 0
            first = ''
            
    if first:
        answer += 1

    return answer
