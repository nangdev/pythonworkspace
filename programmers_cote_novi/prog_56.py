def solution(order):
    ans = 0
    for i in str(order):
        if i == '3' or i == '6' or i == '9':
            ans += 1
    return ans


print(solution(29423))
