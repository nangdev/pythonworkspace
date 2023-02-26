def solution(num, k):
    ans = str(num).find(str(k))+1
    if ans == 0:
        return -1
    return ans


print(solution(123456, 7))
