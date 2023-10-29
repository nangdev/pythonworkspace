t = int(input())
for i in range(1, t+1):
    h, w = map(int, input().split())
    lis = [list(input()) for _ in range(h)]
    lenstr = int(input())
    string = input()

    dx, dy = 0, 0
    cx, cy = 0, 0
    setx, sety = 0, 0
    for a in range(h):
        for b in range(w):
            if '<' == lis[a][b]:
                dx, dy = a, b
                cx, cy = 0, -1
                setx, sety = a, b
                break
            elif '>' == lis[a][b]:
                dx, dy = a, b
                cx, cy = 0, 1
                setx, sety = a, b
                break
            elif '^' == lis[a][b]:
                dx, dy = a, b
                cx, cy = -1, 0
                setx, sety = a, b
                break
            elif 'v' == lis[a][b]:
                dx, dy = a, b
                cx, cy = 1, 0
                setx, sety = a, b
                break

    for comm in string:
        if comm == 'U':
            cx, cy = -1, 0
            dx += cx
            try:
                if lis[dx][dy] == '.':
                    pass
                else:
                    dx -= cx
            except:
                dx -= cx

        elif comm == 'D':
            cx, cy = 1, 0
            dx += cx
            try:
                if lis[dx][dy] == '.':
                    pass
                else:
                    dx -= cx
            except:
                dx -= cx

        elif comm == 'L':
            cx, cy = 0, -1
            dy += cy
            try:
                if lis[dx][dy] == '.':
                    pass
                else:
                    dy -= cy
            except:
                dy -= cy

        elif comm == 'R':
            cx, cy = 0, 1
            dy += cy
            try:
                if lis[dx][dy] == '.':
                    pass
                else:
                    dy -= cy
            except:
                dy -= cy

        else:
            if cx == -1:  # up
                for rune in range(dx, -1, -1):
                    if lis[rune][dy] == '#':
                        break
                    elif lis[rune][dy] == '*':
                        lis[rune][dy] = '.'
                        break

            elif cx == 1:  # down
                for rune in range(dx, h):
                    if lis[rune][dy] == '#':
                        break
                    elif lis[rune][dy] == '*':
                        lis[rune][dy] = '.'
                        break

            elif cy == -1:  # left
                for rune in range(dy, -1, -1):
                    if lis[dx][rune] == '#':
                        break
                    elif lis[dx][rune] == '*':
                        lis[dx][rune] = '.'
                        break

            elif cy == 1:  # right
                for rune in range(dy, w):
                    if lis[dx][rune] == '#':
                        break
                    elif lis[dx][rune] == '*':
                        lis[dx][rune] = '.'
                        break
    if cx == -1:
        lis[dx][dy] = '^'
        lis[setx][sety] = '.'
    elif cx == 1:
        lis[dx][dy] = 'v'
        lis[setx][sety] = '.'
    elif cy == -1:
        lis[dx][dy] = '<'
        lis[setx][sety] = '.'
    elif cy == 1:
        lis[dx][dy] = '>'
        lis[setx][sety] = '.'

    print(f"#{i} ", end="")
    for ans1 in range(h):
        for ans2 in range(w):
            print(f"{lis[ans1][ans2]}", end="")
        print()
