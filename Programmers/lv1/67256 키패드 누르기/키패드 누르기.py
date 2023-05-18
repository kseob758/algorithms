def solution(numbers, hand):
    answer = ''
    dic = {1:[1,1], 2:[1,2], 3:[1,3], 4:[2,1], 5:[2,2], 6:[2,3], 7:[3,1], 8:[3,2], 9:[3,3], 0:[4,2]}
    right, left = [4,3], [4,1]
    
    def touch(hand):
        nonlocal answer, right, left
        if hand == 'R':
            answer += 'R'
            right = dic[num]
        else:
            answer += 'L'
            left = dic[num]

    for num in numbers:
        if num % 3 == 0 and num != 0:
            touch('R')
        elif num % 3 == 1:
            touch('L')
        else:
            right_distance = abs(dic[num][0] - right[0]) + abs(dic[num][1] - right[1])
            left_distance = abs(dic[num][0] - left[0]) + abs(dic[num][1] - left[1])
            if right_distance > left_distance:
                touch('L')
            elif left_distance > right_distance:
                touch('R')
            else:
                if hand == 'right':
                    touch('R')
                else:
                    touch('L')
                       
    return answer
