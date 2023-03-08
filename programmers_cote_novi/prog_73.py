def solution(num, k):
    a = len(num)
    if a % 2 == 0:
        if k <= a // 2:
            return num[2*k-2]
        else:
            return num[k % int(a/2)]
    else:
        if k <= a // 2 + 1:
            return num[2*k-2]
        else:
            if k % a == 0:
                return num[-2]
            if k % a <= a // 2 + 1:
                return num[2*(k % a)-2]
            else:
                return num[2*(k % a)-1]

# def solution(numbers, k):
#    return numbers[2 * (k - 1) % len(numbers)]

# def solution(numbers, k):
#    return 2 * (k - 1) % numbers[-1] + 1


print(solution([1, 2, 3, 4, 5, 6], 5))
