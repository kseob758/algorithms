def solution(id_list, report, k):
    result_cnt = {} # 각 id별 받은 결과 메일 수를 담는 딕셔너리
    report_cnt = {} # 각 id별 신고 당한 횟수를 담는 딕셔너리
    report_list = {} # 각 id별 누가 신고했는지 담는 딕셔너리
    banned = [] # ban 당한 id를 담는 리스트
    
    
    for id in id_list: # 각 dictionary 초기화
        result_cnt[id] = 0
        report_cnt[id] = 0
        report_list[id] = []
        
    report = set(report) # 한 유저가 같은 유저를 여러 번 신고는 불가능 -> 중복 제거
    
    for r in report: # 신고 내용
        r1, r2 = r.split() # r1 신고한 유저, r2 신고 당한 유저
        report_list[r2].append(r1) # r2가 r1에게 신고 당했다는 의미
        report_cnt[r2] += 1 # r2가 신고당한 횟수 +1
        if report_cnt[r2] == k: # k번 신고 당하면 banned list에 추가
            banned.append(r2)
    
    for ban in banned: # banned list에 있는 유저
        for i in report_list[ban]: # 그 유저를 신고한 유저들
            result_cnt[i] += 1 # 결과 메일 받은 횟수 +1
            
    answer = list(result_cnt.values()) # 횟수(dictionary의 value)만 리스트로 변환
    
    return answer
