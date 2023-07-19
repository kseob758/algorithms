def solution(park, routes):
    # 시작 위치(S) 찾기
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] == 'S':
                x, y = j, i
                break
    
    # 이동
    for route in routes:
        # 위치 초기화
        xx = x
        yy = y
        # 이동 - 맵을 벗어나거나 이동할 방향에 장애물이 있으면 무시
        for step in range(int(route[2])):
            # 동쪽 이동
            if route[0] == 'E' and xx != len(park[0])-1 and park[yy][xx+1] != 'X':
                xx += 1
                if step == int(route[2])-1:
                    x = xx
            # 서쪽 이동
            elif route[0] == 'W' and xx != 0 and park[yy][xx-1] != 'X':
                xx -= 1
                if step == int(route[2])-1:
                    x = xx
            # 남쪽 이동
            elif route[0] == 'S' and yy != len(park)-1 and park[yy+1][xx] != 'X':
                yy += 1
                if step == int(route[2])-1:
                    y = yy
            # 북쪽 이동
            elif route[0] == 'N' and yy != 0 and park[yy-1][xx] != 'X':
                yy -= 1
                if step == int(route[2])-1:
                    y = yy  # step만큼 모두 움직였으면 위치 재지정
                    
    return [y, x]  # x, y축과 행, 열 개념 유의
