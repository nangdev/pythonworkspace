n, k = map(int, input().split())
count = 0
while n != 1:
    if n % k == 0:
        while n != 1:
            n /= k
            count += 1
        break
    n -= 1
    count += 1
print(count)

# 해설 본후
# 내 코드는 n이 -1씩 하다가 k의 제곱근이 되어야만 실행됨
# 제곱근이 아니라면 무한루프 발생
# 수정

n, k = map(int, input().split())
count = 0
while n != 1:
    if n % k == 0:
        n /= k
        count += 1
        continue
    n -= 1
    count += 1
print(count)
