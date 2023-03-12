def solution(spell, dic):
    for i in dic:
        a = 0
        for j in spell:
            if j in i:
                a += 1
        if a == len(spell):
            return 1
    return 2
