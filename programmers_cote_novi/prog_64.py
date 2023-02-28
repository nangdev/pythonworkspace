def solution(numlist, n):
    ans = []
    i = 0
    while i != len(numlist):
        ans.append(numlist[i:i+n])
        i += n
    return ans


print(solution([1, 2, 3, 4, 5, 6, 7, 8], 2))
