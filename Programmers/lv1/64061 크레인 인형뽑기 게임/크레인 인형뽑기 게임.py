def solution(board, moves):
    answer = 0
    bucket = []
    for move in moves:
        move = move - 1
        for j in board:
            if j[move] != 0:
                if len(bucket) != 0:
                    if j[move] == bucket[-1]:
                        bucket.pop()
                        answer += 2
                    else:
                        bucket.append(j[move])
                    
                else:
                    bucket.append(j[move])
                j[move] = 0
                break
    return answer
