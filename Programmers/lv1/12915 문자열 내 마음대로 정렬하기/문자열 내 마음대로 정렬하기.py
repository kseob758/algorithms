def solution(strings, n):
    lst = []
    for string in strings:
        lst.append(string[n]+string)
    
    lst.sort()
    
    answer = []
    
    for l in lst:
        answer.append(l[1:])
    return answer
