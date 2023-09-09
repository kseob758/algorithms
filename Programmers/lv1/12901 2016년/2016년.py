def solution(a, b):
    total = 0 # 총 일수
    mon = [0,31,29,31,30,31,30,31,31,30,31,30]  # 1~12월까지의 월별 일수
    day = ['THU','FRI','SAT','SUN','MON','TUE','WED']  # 1일 FRI로 하기 위한 순서
    
    for i in range(a):  # a-1월까지의 일수 더하기
        total += mon[i]
    total += b  # b일 더하기
    
    return day[((total%7))] 
