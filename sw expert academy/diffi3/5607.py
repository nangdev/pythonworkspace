t = int(input())
for i in range(1, t+1):
    N, R = map(int, input().split())

    bunja, bunmo = 1, 1
    for j in range(R):
        bunja *= N-j
        bunmo *= R-j

    ans = bunja // bunmo
    ans = ans % 1234567891
    print(f"#{i} {ans}")

# 테스트 케이스 개수 T 입력 받기
T = int(input())

# 팩토리얼 값을 저장할 리스트 초기화
fact = [1 for _ in range(1000001)]
# 모듈로 연산의 나머지를 구할 때 사용할 값
mod = 1234567891

# 팩토리얼 계산
for i in range(1, 1000001):
    fact[i] = (fact[i-1] * i) % mod

# 테스트 케이스마다 반복
for tc in range(1, T+1):
    # N, R 입력 받기
    N, R = map(int, input().split())
    # N combination R 계산
    denominator = (fact[R] * fact[N-R]) % mod
    result = (fact[N] * pow(denominator, mod-2, mod)) % mod
    print("#{} {}".format(tc, result))
