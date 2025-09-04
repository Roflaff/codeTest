# 테스트 케이스 입력
T = int(input())

for test_case in range(1, T + 1):
    result = 0
    
    # N 입력 
    N = int(input())
    
    # N * N 배열 입력 받기
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    
    print(arr)
    print(f"#{test_case} {result}")