import math


def solution(dots):
    re = []
    val = 0
    answer = 0
    for i in range(4):
        a = dots[i]
        x1 = a[0]
        y1 = a[1]
        for j in range(i):
            if j == i:
                continue
            b = dots[j]
            x2 = b[0]
            y2 = b[1]
            val = (y2-y1) / (x2-x1)
            re.append(val)
    for i in range(len(re)):
        for j in range(i):
            if j == i:
                continue
            if re[i] == re[j]:
                answer = 1
    return answer


print(solution([[1, 4], [9, 2], [3, 8], [10, 4]]))
