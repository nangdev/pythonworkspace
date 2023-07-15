size = int(input())
apple = int(input())
mapping = [[0 for _ in range(size)]for _ in range(size)]

for _ in range(apple):
    n, m = map(int, input().split())
    mapping[n-1][m-1] = 1

direc_count = int(input())
direc = []
for _ in range(direc_count):
    direc.append(list(input().split()))
# 0번째 원소 문자열 int로 써야함
print(mapping)
print(direc)
l, r = 0, 0
time = 0

while True:  # 게임이 끝나는 조건
    pass
