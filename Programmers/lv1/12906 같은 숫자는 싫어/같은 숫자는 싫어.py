def solution(arr):
    answer = []
    num = arr[0]

    for i in range(len(arr)):
        if i == 0:
            answer.append(arr[i])
        elif arr[i] != arr[i-1]:
            answer.append(arr[i])
            
    return answer
