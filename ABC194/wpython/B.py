N = int(input())
A_fastest, A_second = [-1, 1e5], [-1, 1e5]
B_fastest, B_second = [-1, 1e5], [-1, 1e5]
for i in range(N):
    A, B = map(int,input().split())
    if A <= A_fastest[1]:
        A_second = A_fastest
        A_fastest = (i, A)
    elif A <= A_second[1]:
        A_second = (i, A)
    if B <= B_fastest[1]:
        B_second = B_fastest
        B_fastest = (i, B)
    elif B <= B_second[1]:
        B_second = (i, B)
if A_fastest[0] == B_fastest[0]:
    print(min(max(A_fastest[1], B_second[1]), max(B_fastest[1], A_second[1]), A_fastest[1] + B_fastest[1]))
else: print(max(A_fastest[1], B_fastest[1]))