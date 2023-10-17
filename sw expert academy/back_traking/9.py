def dfs(n, sm, add, sub, mul, div):
    global mx, mn
    if n == num:
        mn = min(mn, sm)
        mx = max(mx, sm)
        return

    if add:
        dfs(n+1, sm+numlis[n], add-1, sub, mul, div)
    if sub:
        dfs(n+1, sm-numlis[n], add, sub-1, mul, div)
    if mul:
        dfs(n+1, sm*numlis[n], add, sub, mul-1, div)
    if div:
        dfs(n+1, int(sm/numlis[n]), add, sub, mul, div-1)


t = int(input())
for i in range(1, t+1):
    num = int(input())
    plus, minus, multi, divi = map(int, input().split())
    numlis = list(map(int, input().split()))
    mn = int(1e8)
    mx = int(-1e8)

    dfs(1, numlis[0], plus, minus, multi, divi)

    print(f"#{i} {mx-mn}")
