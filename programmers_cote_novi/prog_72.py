def solution(n):
    ans = [x for x in range(2, n+1) if n % x == 0]
    ans2 = []
    for i in ans:
        count = 0
        for j in range(2, i+1):
            if i % j == 0:
                count += 1
        if count == 1:
            ans2.append(i)
    return ans2


print(solution(420))
