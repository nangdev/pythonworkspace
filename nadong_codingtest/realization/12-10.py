def rotate_a_matrix_by_90(a):
    n = len(a)  # 행 길이 계산
    m = len(a[0])  # 열 길이 계산
    result = [[0]*n for _ in range(m)]  # 결과 리스트
    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = a[i][j]
    return result

# 자물쇠의 중간 부분이 모두 1인지 확인


def check(new_lock):
    lock_length = len(new_lock) // 3
    for i in range(lock_length, lock_length * 2):
        for j in range(lock_length, lock_length*2):
            if new_lock[i][j] != 1:
                return False
        return True


def solution(key, lock):
    n = len(lock)
    m = len(key)
    # 자물쇠의 크기를 기존의 3배로 변환
    new_lock = [[0]*(n*3) for _ in range(n*3)]
    # 새로운 자물쇠의 중앙 부분에 기존의 자물쇠 넣기
    for i in range(n):
        for j in range(n):
            new_lock[i+n][j+n] = lock[i][j]

    # 4가지 방향에 대해서 확인
    for _ in range(4):
        key = rotate_a_matrix_by_90(key)
        for x in range(1, n*2):
            for y in range(1, n*2):
                # 자물쇠에 열쇠를 끼워넣기
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+i] += key[i][j]
                # 새로운 자물쇠에 열쇠가 정확히 들어맞는지 검사
                if check(new_lock) == True:
                    return True

                # 자물쇠에서 열쇠를 다시 빼기
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+i] -= key[i][j]
    return False


def match(arr, key, rot, r, c):
    n = len(key)
    for i in range(n):
        for j in range(n):
            if rot == 0:
                arr[r+i][c+i] += key[i][j]
            elif rot == 1:
                arr[r+i][c+i] += key[n-1-j][i]
            elif rot == 2:
                arr[r+i][c+i] += key[n-1-i][n-1-j]
            else:
                arr[r+i][c+i] += key[j][n-1-i]


def check2(arr, offset, n):
    for i in range(n):
        for j in range(n):
            if arr[offset + i][offset + j] != 1:
                return False
    return True


def solution2(key, lock):
    offset = len(key)-1

    for r in range(offset + len(lock)):
        for c in range(offset + len(lock)):
            for rot in range(4):
                arr = [[0 for _ in range(58)]for _ in range(58)]
                for i in range(len(lock)):
                    for j in range(len(lock)):
                        arr[offset + i][offset + j] = lock[i][j]

                match(arr, key, rot, r, c)
                if check2(arr, offset, len(lock)):
                    return True
    return False
