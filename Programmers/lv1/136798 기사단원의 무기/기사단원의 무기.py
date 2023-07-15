def cnt_divisor(n): # 약수의 개수 구하기
    l = []
    for i in range(1, int(n**0.5) + 1):  # 제곱근 활용하지 않으면 타임아웃
        if n % i == 0:
            l.append(n//i)
            l.append(i)
    return len(set(l))

def solution(number, limit, power):
    answer = 0
    for n in range(number+1):
        num = cnt_divisor(n)
        answer += power if num > limit else num
    return answer
