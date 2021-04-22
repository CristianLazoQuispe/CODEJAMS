T = int(input())
n_A = ord('A')
cnt = 1
while(T):
    
    N = int(input())
    parties = []
    letters = []
    ans = []
    parties = list(map(int,input().split(' ')))
        
    for i in range(N):
        letters.append(n_A+i)
    mean = N/2
    
    parties, letters = zip(*sorted(zip(parties, letters)))
    parties = list(parties)
    letters = list(letters)
    while(parties[-1]>=mean):
        if parties[-1]==0:
            break
        ans.append(chr(letters[-1]))
        parties[-1]-=1
        mean-=0.5
        parties, letters = zip(*sorted(zip(parties, letters)))
        parties = list(parties)
        letters = list(letters)
        #print(parties,letters) 
    solution = 'Case #'+str(cnt)+': '
    for i in ans:
        solution+=i+' '
    print(solution[:-1])
        
        
    cnt+=1
    T-=1


