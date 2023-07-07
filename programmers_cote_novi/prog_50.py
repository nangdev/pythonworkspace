def solution(my_string, n1, n2):
    a = list(my_string)
    a[n1], a[n2] = a[n2], a[n1]
    return ''.join(a)


print(solution("hello", 1, 2))
