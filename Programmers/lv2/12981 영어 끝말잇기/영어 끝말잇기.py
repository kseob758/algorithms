def solution(n, words):
    last = words[0][0]
    already = []
    num, turn = 0, 0
    for i, word in enumerate(words):
        if (word in already) or not(word.startswith(last)):
            num = i % n + 1
            turn = i // n + 1
            break
        already.append(word)
        last = word[-1]    
    
    return [num, turn]
