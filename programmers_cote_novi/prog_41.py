def solution(n, t):
    for i in range(t):
        n *= 2
    return n


def solution2(n, t):
    return n << t  # n의 비트를 t만큼 왼쪽으로 이동인데...
# 2 = 0010  << 10번 10908070605040302010 2의 11승 자리인데
# 맞네 슈발...
# 2진수가 2의 제곱승으로 이동하니 그걸 이용한 코드 미친
# 7 = 0111   0111 0000  16 + 32 + 64 == 112


def solution3(n, t):
    return n*(2**t)


print(solution2(2, 10))
print(2 ** 11)
print(solution2(7, 4))
