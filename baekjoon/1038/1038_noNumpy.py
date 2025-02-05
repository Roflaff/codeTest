# 20240203
# 1038번
# kimsp0317@gamil.com

# N 이 존재하는 행렬 만들기
matrix = [[0] * 10 for _ in range(10)]
matrix[0] = [1] * 10  # 최초 행은 1로 추적

for i in range(1, 10):
    for j in range(1, 10):
        matrix[i][j] = matrix[i][j-1] + matrix[i-1][j-1]

# Input
N = int(input())

def find_X(N, find):
    N_i = 0
    N_j = 0
    matrix_total = 0
    temp = 0
    out = False

    for i in range(10):
        # 현재 행의 크기 합
        temp = sum(matrix[i])
        matrix_total += temp

        # 못 찾을 경우 없는 수
        if N >= sum(sum(row) for row in matrix):
            out = True
            break

        # N이 해당 행보다 크면 다른 행에 N값 존재
        if N > matrix_total - 1:
            pass
        else:
            N_i = i
            find = matrix_total - temp
            for j in range(i, 10):
                if N < find + matrix[i][j]:
                    N_j = j
                    find = N - find
                    break
                find += matrix[i][j]
            break

    return N_i, N_j, find, out

# Output
X = 0
I, J, find, out = find_X(N, 0)

# 범위 이탈
if out:
    print(-1)
    exit()

for i in range(I, -1, -1):
    X = X + 10**I * J
    if i > 1:
        find += sum(sum(matrix[k]) for k in range(i-1))
    I, J, find, out = find_X(find, 0)

print(X)
