def solution(n):
    lst = []
    answer = 0
    while True:
        lst.append(n%3) # 3으로 나눈 나머지를 lst에 추가.
        n = n//3
        if n==0: # 3으로 나눈 몫이 0이면 탈출
            break
    # lst는 이미 앞뒤 반전 3진법 형태
    for i in range(len(lst)):
        answer += lst.pop() * (3**i) # pop()하며 3의 거듭제곱을 곱하여 answer에 합해줌

    return answer
