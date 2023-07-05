def solution(emer):
    ans = []
    cop = emer.copy()
    cop.sort(reverse=True)
    for i in emer:
        for j in cop:
            if i == j:
                ans.append(cop.index(j)+1)
    return ans


print(solution([3, 76, 24]))
