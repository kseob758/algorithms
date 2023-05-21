def solution(answers):
    a = [1,2,3,4,5]
    b = [2,1,2,3,2,4,2,5]
    c = [3,3,1,1,2,2,4,4,5,5]
    
    cnt = [0, 0, 0]
    answer = []
    
    for i in range(len(answers)):
        answer = answers[i]
        if answer == a[i%5]:
            cnt[0] += 1
        if answer == b[i%8]:
            cnt[1] += 1
        if answer == c[i%10]:
            cnt[2] += 1

    answer = [i+1 for i in range(3) if cnt[i] == max(cnt)]
    
    return answer
