def pattern(n):
    a=n//2-1
    for i in range(n):
        if i<n//2:
            if i==0:
                print('*',end='')
                for j in range(a):
                    print(' ',end='')
                for j in range(n//2+1):
                    print('*',end='')
            else:
                print('*',end='')
                for j in range(a):
                    print(' ',end='')
                print('*',end='')
        elif i==n//2:
            for j in range(n):
                print('*',end='')
        elif i>n//2:
            if i==n-1:
                for j in range(n//2+1):
                    print('*',end='')
                for j in range(a):
                    print(' ',end='')
                print('*',end='')
            else:
                for j in range(a+1):
                    print(' ',end='')
                print('*',end='')
                for j in range(a):
                    print(' ',end='')
                print('*',end='')
        print()
pattern(int(input()))
