def solution(num):
    res = ''
    ans = ''
    for i in num:
        res += i
        if res == "zero":
            ans += '0'
            res = ''
        elif res == "one":
            ans += '1'
            res = ''
        elif res == "two":
            ans += '2'
            res = ''
        elif res == "three":
            ans += '3'
            res = ''
        elif res == "four":
            ans += '4'
            res = ''
        elif res == "five":
            ans += '5'
            res = ''
        elif res == "six":
            ans += '6'
            res = ''
        elif res == "seven":
            ans += '7'
            res = ''
        elif res == "eight":
            ans += '8'
            res = ''
        elif res == "nine":
            ans += '9'
            res = ''
    return int(ans)


print(solution("onetwothreefourfivesix"))
