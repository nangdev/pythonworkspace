t = int(input())
for i in range(1, t+1):
    siz = int(input())
    string = input()
    if siz == 1:
        print(f"#{i} No")
        continue
    if string[0:siz//2] == string[siz//2:siz]:
        print(f"#{i} Yes")
    else:
        print(f"#{i} No")
