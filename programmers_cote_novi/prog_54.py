import math


def solution(n):
    return ((n*6)/math.gcd(n, 6)) // 6


# 이런식으로도 최소공배수를 구할 수 있다
def solution1(n):
    answer = 1
    while 6 * answer % n:
        answer += 1
    return answer
