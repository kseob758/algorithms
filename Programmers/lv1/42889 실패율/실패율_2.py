from collections import Counter

def solution(N, stages):
    total_people = len(stages)
    stage_people = Counter(stages)
    fail = {}
    
    for stage in range(1, N+1):
        if total_people > 0:
            fail[stage] = stage_people[stage] / total_people
        else:
            fail[stage] = 0
        total_people -= stage_people[stage]
    
    answer = sorted(fail, key=fail.get, reverse = True)
    
    return answer
