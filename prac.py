def rotate_a_matrix_by_90(a):
    n = len(a)  # 행 길이 계산
    m = len(a[0])  # 열 길이 계산
    result = [[0]*n for _ in range(m)]  # 결과 리스트
    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = a[i][j]
    return result


s = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
for i in s:
    print(i)

se = rotate_a_matrix_by_90(s)
for i in se:
    print(i)
