# 20240203
# 1038번
# kimsp0317@gamil.com

import numpy as np

matrix = np.zeros((10, 10), dtype=int)

# N 이 존재하는 행렬 만들기
for i in range(10) :

    for j in range(10):
        if i == 0:
            matrix[i,j] = 1
        
        if i == j:
            matrix[i,j] = 1
        
        if i > 0 and j > 0 and i <= 10 and j <= 10 :
            matrix[i,j] = matrix[i, j-1] + matrix[i-1, j-1]

# Input
N = int(input())

N_i = 0 
N_j = 0
# 이전 행의 합 값
matrix_total = 0
temp = 0
find = 0

for i in range(10) :
    # 현재 행의 크기 합
    temp = np.sum(matrix[i]) - 1
    matrix_total = matrix_total + temp

    # N이 해당 행보다 크면 다른 행에 N값 존재
    if N > matrix_total :
            pass
    else : 
        N_i = i
        find = matrix_total - temp
        for j in range(10):
            find = find + matrix[i, j]
            if N < find :
                N_j = j
                break
        break

find = find - N

# output
X = 0

