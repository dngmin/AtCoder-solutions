N = int(input())
P_list = [0]*(N+1)
for i, P in enumerate(list(map(int,input().split()))):
    P_list[P] = i
Q = int(input())
for _ in range(Q):
    A, B = map(int,input().split())
    print(A if P_list[A] < P_list[B] else B)