def solution(n):
    num_1 = bin(n).count('1')  # 최초 1의 개수
    while True:
        n += 1
        new_num_1 = bin(n).count('1')  # 숫자를 증가하며 1 개수 체크
        if num_1 == new_num_1:  # 같으면 그 숫자 리
            return n
