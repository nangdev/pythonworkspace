def dfs(n, ch, sm):
    global ans
    if ans <= ch:
        return

    if n == bus[0]:
        ans = min(ans, ch)
        return

    # dfs(n+1, ch+1, bus[n]-1)  이렇게하면 시간이 훨씬 오래걸림
    # 유망한 쪽으로 호출을 먼저 하는게 유리하다
    if sm > 0:
        dfs(n+1, ch, sm-1)
    dfs(n+1, ch+1, bus[n]-1)


t = int(input())
for i in range(1, t+1):
    bus = list(map(int, input().split()))
    ans = 51
    dfs(2, 0, bus[1]-1)
    print(f"#{i} {ans}")
