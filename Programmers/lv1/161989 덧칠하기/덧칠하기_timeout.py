# 처음에 생각했던 filter 활용 방법
def solution(n, m, section):
    answer = 0
    while section:
        section = list(filter(lambda x: x>=section[0]+m, section))  # 모든 원소를 살펴야 해서 시간 복잡도 증가
        answer += 1
    return answer
