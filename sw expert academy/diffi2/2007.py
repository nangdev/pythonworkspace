n = int(input())
for i in range(n):
    lis = list(input())
    cop = []
    for j in range(len(lis)):
        cop.append(lis[j])
        if cop == lis[j+1:j+1+len(cop)]:
            print(f"#{i+1} {len(cop)}")
            break
