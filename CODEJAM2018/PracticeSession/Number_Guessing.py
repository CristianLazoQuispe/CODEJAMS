import sys

T = int(input())
while(T):
    a = (input()).split(' ')
    low = int(a[0])
    upper = int(a[1])
    _ = int(input())

    while(low<=upper):
        median = (low+upper)//2
        print(median)
        sys.stdout.flush()
        ans = input()
        if ans == 'CORRECT':
            break
        elif ans == 'TOO_SMALL':
            low = median+1
        else:
            upper = median-1
    #print(0)
    T-=1


