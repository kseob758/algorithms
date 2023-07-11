# section을 1회만 순회하는 방법
def solution(n, m, section):
    cnt = 0
    start = 0
    for s in section:
        if s > start:  # 롤러를 다시 사용해야하는 경우
            cnt += 1
            start = s + m - 1
    return cnt
