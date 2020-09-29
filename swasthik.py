n = int(input('Enter value of n: '))

for i in range(1,2*n):
    for j in range(1,2*n):
        if i==n or j==n:
            print('*', end='')
        elif i< n and j==1:
            print('*', end='')
        elif i==1 and j >n:
            print('*', end='')
        elif i>n and j==2*n-1:
            print('*', end='')
        elif i==2*n-1 and j< n:
            print('*', end='')
        else:
            print(' ', end='')
    print()
