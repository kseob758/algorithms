# 슬라이싱이 pop or del 활용보다 느리다.
def solution(ingredient):
    l = []
    answer = 0
    for i in ingredient:
        l.append(i)
        if l[-4:] == [1, 2, 3, 1]:
            answer += 1
            del l[-4:]  # 이 부분 l = l[-4:] (슬라이싱 활용)하면 타임아웃
    return answer
