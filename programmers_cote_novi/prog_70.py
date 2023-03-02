def solution(bin1, bin2):
    ans = bin(int(bin1, 2)+int(bin2, 2))
    return ans[2:]
