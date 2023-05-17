from itertools import combinations

def solution(numbers):
    answer = []
    lst = list(combinations(numbers,2)) # 2개의 숫자를 선택해 나오는 조합(num1,num2) 리스트
    
    for i in lst: # 각 쌍의 합을 answer에 append
        answer.append(sum(i))
        
    answer = list(set(answer)) # 중복을 제거한 리스트로 변경
    answer.sort() # 오름차순 정렬
    
    return answer
