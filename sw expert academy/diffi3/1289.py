t = int(input())
for i in range(1, t+1):
    mem = input()
    mem_n = len(mem)
    result = ['0']*mem_n
    count = 0

    for j in range(mem_n):
        if mem[j] != result[j]:
            if mem[j] == '1':
                for k in range(j, mem_n):
                    result[k] = '1'
                count += 1
            else:
                for k in range(j, mem_n):
                    result[k] = '0'
                count += 1
    print(f"#{i} {count}")
