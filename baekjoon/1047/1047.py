"""
5
1 1 1
2 8 1
8 2 1
9 9 1
5 5 32

5
1 3 4
9 2 4
8 1 4
9 7 4
5 5 4
"""
def find_max_x(spot, N: int):
    max_index = 0
    temp = spot[0][0]
    for i in range(N):
        if spot[i][0] > temp:
            temp = spot[i][0]
            max_index = i
    
    return max_index

def find_max_y(spot, N: int):
    max_index = 0
    temp = spot[0][1]
    for i in range(N):
        if spot[i][1] > temp:
            temp = spot[i][1]
            max_index = i
    
    return max_index

def find_min_x(spot, N: int):
    min_index = 0
    temp = spot[0][0]
    for i in range(N):
        if spot[i][0] < temp:
            temp = spot[i][0]
            min_index = i
    
    return min_index

def find_min_y(spot, N: int):
    min_index = 0
    temp = spot[0][1]
    for i in range(N):
        if spot[i][1] < temp:
            temp = spot[i][1]
            min_index = i
    
    return min_index

def get_len(max, min):
    return max - min

def find_total_len(max_x, max_y, min_x, min_y):
    w = max_x - min_x
    h = max_y - min_y
    return 2 * (w + h)

def find_remove_tree(spot, len, N):
    
    # 사용 가능한 나무 길이
    total_tree_len = 0
    
    for i in range(N):
        total_tree_len += len[i]
    
    max_x = find_max_x(spot=spot, N=N)
    max_y = find_max_y(spot=spot, N=N)
    min_x = find_min_x(spot=spot, N=N)
    min_y = find_min_y(spot=spot, N=N)

    total_len = find_total_len(
        max_x=spot[max_x][0],
        max_y=spot[max_y][1],
        min_x=spot[min_x][0],
        min_y=spot[min_y][1]
    )
    
    if total_tree_len < total_len:
        return False
    else:
        return True

### 시작

# --- 입력 ---
N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

spot = [[0]*2 for _ in range(N)]
len = [0] * N

for a, i in zip(arr, range(N)):
    len[i] = a[2]
    spot[i] = a[:2]

# --- 처리 ---
for i in range(N):
    total_tree_len += len[i]
