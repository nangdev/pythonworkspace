def solution(n):
    ans = 1
    i = 0
    while ans <= n:
        i += 1
        ans *= i
    return i-1


print(solution(7))
