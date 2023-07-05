def solution(i, j, k):
    ans = 0
    for i in range(i, j+1):
        for n in str(i):
            if n == str(k):
                ans += 1
    return ans


print(solution(1, 13, 1))
