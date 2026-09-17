N = int(input())
L_list = list(map(int,input().split()))
output = 0
for a in range(N-2):
    for b in range(a+1,N-1):
        for c in range(b+1,N):
            La, Lb, Lc = L_list[a], L_list[b], L_list[c]
            if La == Lb or La == Lc or Lb == Lc: continue
            max_L = max(La, Lb, Lc)
            if sum([La,Lb,Lc]) - max_L > max_L:
                output += 1
print(output)