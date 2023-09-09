def solution(a, b):
    total = 0
    mon = [0,31,29,31,30,31,30,31,31,30,31,30]
    day = ['THU','FRI','SAT','SUN','MON','TUE','WED']
    
    for i in range(a):
        total += mon[i]
    total += b
    
    return day[((total%7))] 
