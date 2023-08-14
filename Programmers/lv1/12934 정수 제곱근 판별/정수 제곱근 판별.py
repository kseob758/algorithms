import math as m

def solution(n):
    return (m.sqrt(n)+1)**2 if m.sqrt(n) % 1 == 0 else -1
