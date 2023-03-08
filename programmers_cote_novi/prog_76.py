import math


def solution(strr, n):
    ans = []
    s = n
    for i in range(math.ceil(len(strr)/n)):
        ans.append(strr[i*n:s])

        s += n
    return ans
 #   0 2 3 5 6 8


print(solution("abc1Addfggg4556b", 6))
