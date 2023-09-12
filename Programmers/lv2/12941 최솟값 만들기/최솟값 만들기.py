def solution(A,B):
    sorted_A = sorted(A)
    sorted_B = sorted(B, reverse=True)
    answer = 0

    for i, j in zip(sorted_A, sorted_B):
        answer += i*j
    return answer
