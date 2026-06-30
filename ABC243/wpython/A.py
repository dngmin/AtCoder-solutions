V, A, B, C = map(int,input().split())
V %= A + B + C
if V >= A:
    V -= A
    if V >= B:
        print("T")
    else:
        print("M")
else:
    print("F")