def solution(arr, n):
    arr.sort()
    ans = 0
    minus = 100
    for i in arr:
        if abs(n-i) < minus:
            ans = i
        minus = abs(n-i)
    return ans


print(solution([15, 11, 13], 14))


# 테케3 [9, 11, 12] 10 9
# 테케4 [15, 11, 13] 14 13
