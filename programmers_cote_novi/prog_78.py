import math


def solution(balls, sha):
    return int(math.factorial(balls)/(math.factorial(sha)*math.factorial(balls-sha)))


print(solution(5, 3))
