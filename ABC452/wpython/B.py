H, W = map(int,input().split())
for i in range(H):
    print("#"*W if i == 0 or i == H-1 else "#"+"."*(W-2)+"#")