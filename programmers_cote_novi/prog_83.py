def solution(dots):
    dots.sort()
    return abs((dots[1][1]-dots[0][1]) * (dots[2][0]-dots[0][0]))


li = [[-1, -1], [1, 1], [1, -1], [-1, 1]]
li.sort()
print(solution(li))
