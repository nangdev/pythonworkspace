def solution(n, t):
    for i in range(t):
        n *= 2
    return n


def solution2(n, t):
    return n << t


def solution3(n, t):
    return n*(2**t)
