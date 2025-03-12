
size = 6
for i in range(size) :
    
    for j in range(size - i - 1) :
        print(' ', end = ' ')

    for j in range(i + 1) :
        print('1', end = ' ')
        break

    for j in range(i) :
        print(' ', end = ' ')
    ############
    for j in range(0, i - 1) :
        print(' ', end = ' ')

    for j in range(i + 1) :
        if i == 0 :
            break
        print('1', end = ' ')
        break
    
    for j in range(i, size -1) :
        print(' ', end=' ')

    if i == size :
        break
    print('\n')

#####
    
for i in range(size) :
    
    for j in range(1, i + 1) :
        print(' ', end = ' ')

    for j in range(i, size) :
        if i == 0 :
            break

        print('1', end=' ')
        break
        
    for j in range(size - i - 1, 0, -1) :
        if i == 0 :
            break
        print(' ', end = ' ')

    ###

    for j in range(size - 2 - i, 0, -1) :
        if i == 0 :
            break
        print(' ', end = ' ')

    for j in range(i, size-1) :
        if i == 0 :
            break

        print('1', end=' ')
        break

    for j in range(i):
        print(' ', end = ' ')
    
    if i != 0 :
        print('\n')

# for i in range(size -1) :

#     for j in range(i) :
#         print(0, end = ' ')
    
#     print('\n')