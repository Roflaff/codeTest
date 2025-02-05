# 20240203
# 1038번
# kimsp0317@gamil.com

import numpy as np

# N 이 존재하는 행렬 만들기
matrix = np.zeros((10, 10), dtype=int)
matrix[0] = 1
for i in range(10) :
    for j in range(10):
        if i > 0 and j > 0 and i <= 10 and j <= 10 :
            matrix[i,j] = matrix[i, j-1] + matrix[i-1, j-1]

# Input
N = int(input())

def find_X(N, find) :
    N_i = 0 
    N_j = 0
    matrix_total = 0
    temp = 0
    N = N
    find = find
    out = False

    for i in range(10) :
        # 현재 행의 크기 합
        temp = np.sum(matrix[i])
        matrix_total = matrix_total + temp

        # 못 찾을 경우 없는 수
        if N > np.sum(matrix):
            out = True
            break

        # N이 해당 행보다 크면 다른 행에 N값 존재
        if N > matrix_total - 1:
            pass
        else : 
            N_i = i
            find = matrix_total - temp
            for j in range(i, 10):
                if N < find + matrix[i, j] :
                    N_j = j
                    find = N - find
                    break
                find = find + matrix[i, j]
            break

    return N_i, N_j, find, out

# output
X = 0
I, J, find, out = find_X(N, 0)

# 범위 이탈
if out is True:
    print(int(-1))
    exit()

for i in range(I, -1, -1) :
    X = X + 10**I * J
    if find == 0:
        break
    if i > 1 :
        find = find + np.sum(matrix[:i-1])
    I, J, find, out = find_X(find, 0)

print(X)