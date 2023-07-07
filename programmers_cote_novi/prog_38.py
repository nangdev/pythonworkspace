def solution(my_string):
    answer = my_string.maketrans({'a': '',
                                  'e': '',
                                  'i': '',
                                  'o': '',
                                  'u': ''})
    return my_string.translate(answer)


print(solution("bus"))
