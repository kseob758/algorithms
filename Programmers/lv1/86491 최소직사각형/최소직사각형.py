def solution(sizes):
    width = []
    height = []
    
    for size in sizes: # 각 가로 세로 쌍에서
        width.append(max(size)) # 큰 값을 width에 추가
        height.append(min(size)) # 작은 값은 height에 추가
        
    result = max(width) * max(height) # width 중 max, height 중 max 곱
    return result
