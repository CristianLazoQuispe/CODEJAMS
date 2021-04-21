def inputi():
    return int(input())
def inputli():
    return list(map(int,input().split(' ')))
def inputls():
    return list(map(str,input().split(' ')))


def solve_sub(ref,sizes):
    for idx,i in enumerate(sizes):
        if (ref>i):
            ref = ref+i
        else:
            bandera = True
            cnt_aux = 0
            aux = 0

            aux1 = ref
            while(bandera):
                aux1 =aux1 + (aux1-1)
                cnt_aux+=1
                if(aux1>i):
                    bandera = False
            return min(cnt_aux+solve_sub(aux1+i,sizes[idx+1:]),len(sizes)-idx)
    return 0
def solve():

    lista = inputli()
    ref = lista[0] 

    sizes = inputli()
    sizes = sorted(sizes)

    ans = 0

    if ref ==1 :
        return len(sizes)
    

    ans = min(solve_sub(ref,sizes),len(sizes))
    
    return ans


t = inputi()


for i in range(t):

    ans = solve()
    print("Case #"+str(i+1)+': '+str(ans),end='')
    print('') if i!=(t-1) else None