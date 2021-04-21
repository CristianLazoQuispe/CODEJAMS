def inputi():
    return int(input())
def inputli():
    return list(map(int,input().split(' ')))
def inputls():
    return list(map(str,input().split(' ')))


def print_list(lista):
    s=""
    for i in lista[:-1]:
        s+=str(i)+" "
    s+=str(lista[-1])

    return s


def solve():

    return [20,40,60]


t = inputi()


for i in range(t):

    ans = solve()
    print("Case #"+str(i+1)+':',print_list(ans),end='')
    #print("Case #"+str(i+1)+':',ans,end='')
    print('') if i!=(t-1) else None
