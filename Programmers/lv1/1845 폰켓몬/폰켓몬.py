def solution(nums):
    pick = len(nums) // 2
    s = set(nums)
    return len(s) if len(s) <= pick else pick
