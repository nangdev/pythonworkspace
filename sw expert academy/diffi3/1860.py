t = int(input())
for i in range(1, t+1):
    people, time, fish = map(int, input().split())
    arrive = list(map(int, input().split()))
    arrive.sort()

    cur_fish = 0
    flag = 0
    for k in range(arrive[-1]+1):
        if k % time == 0:
            if k != 0:
                cur_fish += fish

        if k in arrive:
            cur_fish -= 1
            if cur_fish < 0:
                print(f"#{i} Impossible")
                flag = 1
                break
    if flag == 0:
        print(f"#{i} Possible")
