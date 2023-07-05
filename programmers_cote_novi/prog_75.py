def solution(s):
    se = s.split()
    ans = []
    for i in se:
        if i == 'Z':
            ans.pop()
            continue
        ans.append(int(i))
    return sum(ans)
