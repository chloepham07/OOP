n= int(input('input n '))
for i in range (0,n):
    for j in range (i,n):
         print(' ', end='')
    for j in range(0,i):
        print('*',end=" ")
    print()
for i in range (0,n):
    for j in range (0,i): print(' ',end='')
    for j in range (i,n): print('*',end=' ')
    print()