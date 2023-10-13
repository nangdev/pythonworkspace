def dfs(num, sum):
    global ans
    if num == n:
        ans = min(ans, sum)
        return

    for j in range(n):
        # 방문 리스트 꼭 초기화처리
        if v[j] == 0:
            v[j] = 1
            dfs(num+1, sum+lst[num][j])
            v[j] = 0


t = int(input())
for i in range(1, t+1):
    n = int(input())
    lst = []
    for _ in range(n):
        lst.append(list(map(int, input().split())))

    ans = 100
    v = [0]*n
    dfs(0, 0)

    print(f"{i} {ans}")
