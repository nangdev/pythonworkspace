def solution(strr):
    res = strr.split()
    ans = int(res[0])
    for i in range(1, len(res), 2):
        if res[i] == '+':
            ans += int(res[i+1])
        elif res[i] == '-':
            ans -= int(res[i+1])
    return ans


print(solution("1 + 2 + 3 + 4"))
