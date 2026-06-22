N, A, B = map(int,input().split())
if N %2 == 0:
    t = ("."*B + "#"*B) * (N//2)
    f = ("#"*B + "."*B) * (N//2)
else:
    t = ("."*B + "#"*B) * (N//2) + "." * B
    f = ("#"*B + "."*B) * (N//2) + "#" * B
tf = True
i = 0
for c in range(N*A):
    if i == A:
        i = 0
        tf = False if tf else True
    print(t if tf else f)
    i+=1