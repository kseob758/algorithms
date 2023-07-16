def solution(ingredient):
    l = []
    answer = 0
    for i in ingredient:
        l.append(i)
        if l[-4:] == [1, 2, 3, 1]:
            answer += 1
            del l[-4:]
    return answer
