def solution(n):
    return [x+1 for x in range(n) if n % (x+1) == 0]


print(solution(24))
