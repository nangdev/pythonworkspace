t = int(input())
for i in range(1, t+1):
    L, U, X = map(int, input().split())

    if L <= X <= U:
        print(f"#{i} {0}")
    elif X < L:
        print(f"#{i} {L-X}")
    elif X > U:
        print(f"#{i} {-1}")
