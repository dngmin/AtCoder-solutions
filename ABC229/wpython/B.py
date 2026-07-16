A, B = input().split()
size = min(len(A), len(B))
for i in range(1,size+1):
    if int(A[-i]) + int(B[-i]) >= 10:
        print("Hard")
        break
else:
    print("Easy")