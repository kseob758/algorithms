def date_to_days(date):
    '''날짜를 일 단위로 변환'''
    year, month, day = map(int, date.split('.'))
    return (year * 12 * 28) + (month * 28) + day
    
def solution(today, terms, privacies):
    answer = []

    today = date_to_days(today)

    terms_dict = dict()
    for term in terms:
        term = term.split()
        terms_dict[term[0]] = int(term[1]) * 28
            
    for n, privacy in enumerate(privacies):
        date, t = privacy.split()
        limit = date_to_days(date) + terms_dict[t]  # 보관 가능한 날짜
        if limit <= today:  # 파기해야 할 경우
            answer.append(n+1)
        
    return answer
