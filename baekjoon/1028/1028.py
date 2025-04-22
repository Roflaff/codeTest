#1028

# 입력
R, C = map(int, input().split())
array = [[0 for j in range(C)] for i in range(R)]

for r in range(R) :
    temp = input()
    for c in range(C) :
        array[r][c] = int(temp[c])

# 해당 배열에서 존재할 수 있는 다이아의 최대 사이즈 찾기
def diaMaxSize(R, C) :
    return int((min(R, C) + 1 ) / 2)

# 다이아 배열 생성 및 반환 사이즈로 반환해줌
def createDia(size) :
    lenth = size*2 - 1
    dia = [[0 for j in range(lenth)] for i in range(lenth)]
    
    for i in range(size) :
        temp = ""
        for j in range(size - i - 1) :
            temp = temp + "0"

        for j in range(i + 1) :
            temp = temp + "1"
            break

        for j in range(i) :
            temp = temp + "0"
        
        ############
        for j in range(0, i - 1) :
            temp = temp + "0"

        for j in range(i + 1) :
            if i == 0 :
                break
            temp = temp + "1"
            break
        
        for j in range(i, size -1) :
            temp = temp + "0"

        for k in range(lenth):
            dia[i][k] = int(temp[k])

        if i == size :
            break

    for i in range(size) :
        temp = ""
        for j in range(1, i + 1) :
            temp = temp + "0"

        for j in range(i, size) :
            if i == 0 :
                break

            temp = temp + "1"
            break
            
        for j in range(size - i - 1, 0, -1) :
            if i == 0 :
                break
            temp = temp + "0"

        ###

        for j in range(size - 2 - i, 0, -1) :
            if i == 0 :
                break
            temp = temp + "0"

        for j in range(i, size-1) :
            if i == 0 :
                break

            temp = temp + "1"
            break

        for j in range(i):
            temp = temp + "0"
        
        start = size + i - 1
        for k in range(lenth):
            if i == 0 :
                break

            dia[start][k] = int(temp[k])

    return dia, lenth

# 다이아의 최대 크기는 R, C 에 영향을 받는다
def findMaxDia(R, C, array, dia) :
    max_size = diaMaxSize(R, C)
    
    find = False
    while find != True :
        dia, lenth_dia = createDia(max_size)
        split_arrays = [ [row[i:i+3] for row in array] for i in range(lenth_dia) ]
        for I in range(R - lenth_dia) :
            for J in range(C - lenth_dia) :

        
    return max_size

initSize = diaMaxSize(R, C)
initDia = createDia(initSize)

print(findMaxDia(R, C, array, initDia))