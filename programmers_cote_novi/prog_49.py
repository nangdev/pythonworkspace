from itertools import *


def solution(numbers):
    return max([c[0] * c[1] for c in list(combinations(numbers, 2))])


# 위에 코드는 좀 개같은 코드고 밑에 코드를 잘 복기하자
# 최댓값, 최솟값 문제에서는 항상 정렬을 한 뒤에 시도해보자

def solution1(numbers):
    numbers = sorted(numbers)
    return max(numbers[0] * numbers[1], numbers[-1]*numbers[-2])
