N = int(input())
S = input()
for i in range(1,N):
    for l in range(0,N-i):
        if S[l] == S[l+i]:
            print(l)
            break
    else:
        print(l+1)