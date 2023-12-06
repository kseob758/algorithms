def solution(s):
    stack = []
    for x in s:
        stack.append(x)
        if len(stack) > 1 and stack[-1] == stack[-2]:
            stack.pop()
            stack.pop()

    if len(stack) == 0:  # 모두 제거
        return 1
    else:  # 제거 불가
        return 0
