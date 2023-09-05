# timeout code : O(n^2)
def solution(numbers):
    answer = []
    for i, num in enumerate(numbers):
        dcs = -1
        for j in range(i, len(numbers)):
            if numbers[j] > num:
                dcs = numbers[j]
                break
        answer.append(dcs)
        
    return answer
