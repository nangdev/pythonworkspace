def solution(string):
    li = [int(i) for i in string if i.isdigit()]
    li.sort()
    return li


print(solution("hi12392"))
