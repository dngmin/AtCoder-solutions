A, B, C, D = map(int,input().split())
if C*D - B <= 0: print(-1)
else:
    output = A / (C*D-B)
    if output % 1 != 0: output = (output + 1) // 1
    print(int(output))