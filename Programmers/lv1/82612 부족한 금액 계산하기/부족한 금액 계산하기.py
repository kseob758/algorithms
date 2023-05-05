def solution(price, money, count):

    total = 0
    while count>=1:
        total += price*count
        count -= 1

    if money >= total:
        return 0
    
    return total-money
