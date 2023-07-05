def solution(chik):
    ans = 0
    ans2 = chik
    ansre = 0
    for i in range(1, len(str(chik))):
        ans += ans2 // 10
        if ans2 % 10 == 0:
            ansre += 1
        else:
            ansre += ans2 % 10
        ans2 //= 10
    for i in range(1, len(str(ansre))):
        ans += ansre // 10
    return ans


def solution1(chicken):
    answer = 0
    coupon = chicken

    while coupon >= 10:
        eaten = coupon//10
        answer += eaten
        coupon = coupon % 10 + eaten
    return answer


print(int(100 * 0.111111))
