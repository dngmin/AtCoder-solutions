A, B = map(int,input().split())
if abs(A-B) == 1:
    if not min(A,B) in [3,6]:
        print("Yes")
        exit()
print("No")