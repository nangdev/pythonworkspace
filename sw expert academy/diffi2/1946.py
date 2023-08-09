t = int(input())
for i in range(t):
    numnum = int(input())
    answer = ""
    ran = 0
    for j in range(numnum):
        al = list(input().split())
        answer += al[0]*int(al[1])
        ran += int(al[1])
    print(f"#{i+1}")
    for k in range(0, ran, 10):
        print(answer[k:k+10])
