def solution(age):
    di = {}
    a = 97
    for i in range(10):
        di[i] = chr(a)
        a += 1

    ans = list(str(age))
    answer = ''

    for i in range(len(ans)):
        answer += di[int(ans[i])]

    return answer


print(solution(23))
