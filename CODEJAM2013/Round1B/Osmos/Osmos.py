def inputi():
    return int(input())
def inputli():
    return list(map(int,input().split(' ')))
def inputls():
    return list(map(str,input().split(' ')))



def solve():
    lista = inputli()
    ref = lista[0] 
    sizes = inputli()
    sizes = sorted(sizes)

    ans = 0

    if ref ==1 :
        return len(sizes)
    #print(ref,sizes)
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
                #print(aux1,i)
                if(aux1>i):
                    bandera = False
            if cnt_aux>=(len(sizes)-idx):
                ans += (len(sizes)-idx)
                break
            else:
                ans += cnt_aux
                ref = aux1+i
        #print(i,ref)

    return ans


t = inputi()


for i in range(t):

    ans = solve()
    print("Case #"+str(i+1)+': '+str(ans),end='')
    print('') if i!=(t-1) else None