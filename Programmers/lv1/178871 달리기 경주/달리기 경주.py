def solution(players, callings):
    race = {j:i for i, j in enumerate(players)}  # 이름:등수
    for call in callings:
        rank = race[call]  # 등수
        race[players[rank]] -= 1  # 딕셔너리의 등수 변경
        race[players[rank-1]] += 1
        players[rank], players[rank-1] = players[rank-1], players[rank]  # 순서 변경
    return players

# 딕셔너리 없이 리스트 + index메소드 쓰면 시간 초과
