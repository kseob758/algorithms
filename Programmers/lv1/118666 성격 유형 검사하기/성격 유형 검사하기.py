def solution(survey, choices):
    answer = ''
    d = {'R':0, 'T':0,
         'C':0, 'F':0,
         'J':0, 'M':0,
         'A':0, 'N':0
        }
    for s, c in zip(survey, choices):
        if c >= 4:
            d[s[1]] += c - 4
        else:
            d[s[0]] += 4 - c
    
    answer += 'R' if d.get('R') >= d.get('T') else 'T'
    answer += 'C' if d.get('C') >= d.get('F') else 'F'
    answer += 'J' if d.get('J') >= d.get('M') else 'M'
    answer += 'A' if d.get('A') >= d.get('N') else 'N'
    return answer
