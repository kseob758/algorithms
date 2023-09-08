import collections
import copy
import itertools
import sys
input = sys.stdin.readline


def calculate_area_size():
    '''안전 영역 크기 확인'''
    q = collections.deque(virus)
    check_map = copy.deepcopy(lab_map)

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m or check_map[nx][ny] != 0:
                continue
            check_map[nx][ny] = 2  # virus spread
            q.append((nx, ny))

    global answer
    cnt = 0
    for c in check_map:
        cnt += c.count(0)
    answer = max(answer, cnt)


n, m = map(int, input().split())
lab_map = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

blank, virus = [], []
for x in range(n):
    for y in range(m):
        if lab_map[x][y] == 0:
            blank.append((x, y))
        elif lab_map[x][y] == 2:
            virus.append((x, y))

answer = 0
for blank in itertools.combinations(blank, 3):
    for wx, wy in blank:
        lab_map[wx][wy] = 1
    calculate_area_size()
    for wx, wy in blank:
        lab_map[wx][wy] = 0
        
print(answer)
