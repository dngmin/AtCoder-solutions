N = int(input())
A_list = list(map(int,input().split()))
B_list = list(map(int,input().split()))
C_list = list(map(int,input().split()))
satisfaction = 0
A_before = -1
for A in A_list:
    satisfaction += B_list[A-1]
    if A_before+1 == A:
        satisfaction += C_list[A-2]
    A_before = A
print(satisfaction)