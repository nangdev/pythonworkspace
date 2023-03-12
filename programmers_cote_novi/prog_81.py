def solution(key, board):
    ans = [0, 0]
    for i in key:
        if abs(ans[0]) == board[0] // 2 or abs(ans[1]) == board[1] // 2:
            return ans
        if i == "left":
            ans[0] -= 1
        elif i == "right":
            ans[0] += 1
        elif i == "up":
            ans[1] += 1
        elif i == "down":
            ans[1] -= 1
    return ans


def solutionB(keyinput, board):
    col = board[0]
    row = board[1]
    result = [0, 0]
    for i in keyinput:
        if i == "left" and result[0]-1 >= -(col // 2):
            result[0] -= 1
        elif i == "right" and result[0]+1 <= (col // 2):
            result[0] += 1
        elif i == "up" and result[1]+1 <= (row // 2):
            result[1] += 1
        elif i == "down" and result[1]-1 >= -(row // 2):
            result[1] -= 1
    return result
