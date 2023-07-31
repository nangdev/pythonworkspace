# n = int(input())
# for i in range(n):
#     stu_ran, stu_num = map(int, input().split())
#     score_lis = {}
#     for j in range(stu_ran):
#         score = list(map(int, input().split()))
#         score_lis[j+1] = round((score[0]*35/100) +
#                                (score[1]*45/100) + (score[2]*20/100), 1)
#     score_lis = dict(
#         sorted(score_lis.items(), key=lambda x: x[1], reverse=True))
#     print(score_lis)

for t in range(int(input())):
    n, k = map(int, input().split())
    score = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    arr = []
    for _ in range(n):
        a, b, c = map(int, input().split())
        value = (a*0.35) + (b*0.45) + (c*0.20)
        arr.append(value)
    k_score = arr[k-1]
    arr.sort(reverse=True)
    x = n // 10
    result = arr.index(k_score)//x
    print(f'#{t+1} {score[result]}')
