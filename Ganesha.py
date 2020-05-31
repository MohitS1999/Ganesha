#For n is EVEN
def pattern(n):

    a=n//2-1

    #for upper block

    for i in range(n+1):

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

        #For Mid Line

        elif i==n//2:

            for j in range(n+1):

                print('*',end='')

        #for Lower Block

        elif i>n//2:

            if i==n:

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
##*    ******
##*    *
##*    *
##*    *
##*    *
##***********
##     *    *
##     *    *
##     *    *
##     *    *
##******    *
