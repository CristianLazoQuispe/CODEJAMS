def inputi():
    return int(input())
def inputli():
    return list(map(int,input().split(' ')))
def inputls():
    return list(map(str,input().split(' ')))



def solve():

    return 20


t = inputi()


for i in range(t):

    ans = solve()
    print("Case #"+str(i+1)+':',ans,end='')
    print('') if i!=(t-1) else None