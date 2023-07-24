n = int(input())
for i in range(n):
    stu_ran, stu_num = map(int, input().split())
    score_lis = []
    for j in range(stu_ran):
        score_lis.append(list(map(int, input().split())))
    grade = (score_lis[stu_num-1][0] / 100 * 35) + \
        (score_lis[stu_num-1][1] / 100 * 45) + \
        (score_lis[stu_num-1][2] / 100 * 20)
    if grade > 90:
        print(f"#{i+1} A+")
    elif grade <= 90 and grade > 80:
        print(f"#{i+1} A0")
    elif grade <= 80 and grade > 70:
        print(f"#{i+1} A-")
    elif grade <= 70 and grade > 60:
        print(f"#{i+1} B+")
    elif grade <= 60 and grade > 50:
        print(f"#{i+1} B0")
    elif grade <= 50 and grade > 40:
        print(f"#{i+1} B-")
    elif grade <= 40 and grade > 30:
        print(f"#{i+1} C+")
    elif grade <= 30 and grade > 20:
        print(f"#{i+1} C0")
    elif grade <= 20 and grade > 10:
        print(f"#{i+1} C-")
    else:
        print(f"#{i+1} D0")
