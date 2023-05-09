def solution(absolutes, signs):
    answer = sum(num if sign else -num for num, sign in zip(absolutes, signs))       
    return answer
