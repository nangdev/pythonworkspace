def solution(s):
    ans = ''
    li = [i for i in s if s.count(i) == 1]
    li.sort()
    for i in li:
        ans += i
    return ans


print(solution("abcabcadc"))
