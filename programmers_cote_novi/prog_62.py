def solution(bef, aft):
    ans1 = list(bef)
    ans2 = list(aft)
    if sorted(ans1) == sorted(aft):
        return 1
    return 0
