def solution(keymap, targets):
    answer = []
    d = dict()  # key : 각 알파벳, value : 최소 클릭 수
    for key in keymap:
        for idx, k in enumerate(key):
            num = d.get(k)
            if num:
                d[k] = min(num, idx+1)
            else:
                d[k] = idx+1
    
    for target in targets:
        total = 0
        for c in target:
            click = d.get(c)
            if click:
                total += click
            else:
                total = -1
                break
        answer.append(total)
            
    return answer
