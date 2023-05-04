def solution(numbers):
    total = 0
    num_lst = list(range(0,10))
    for num in num_lst:
        if num not in numbers:
            total += num
    return total
