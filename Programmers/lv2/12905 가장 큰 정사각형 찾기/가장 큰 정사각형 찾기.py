def solution(board):
    dp = [[0]* (len(board[0])+1) for _ in range(len(board)+1)]
    answer = 0
    for i in range(0, len(board)):
        for j in range(0, len(board[0])):

            if board[i][j] == 1:
                dp[i+1][j+1] = min(dp[i][j+1], dp[i+1][j], dp[i][j]) + 1

                if dp[i+1][j+1] > answer :
                    answer = dp[i+1][j+1]

    return answer**2
