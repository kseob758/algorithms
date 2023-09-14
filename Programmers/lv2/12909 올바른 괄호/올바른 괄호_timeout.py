# 정확성 성공 효율성 실패
def solution(s):
    while '()' in s:
        s = s.replace('()', '')  # '()'가 없을 때까지 제거
        
    return False if s else True
