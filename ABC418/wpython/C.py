import bisect

N, Q = map(int,input().split())
A_list = list(map(int,input().split()))
A_list.sort()
prefix_sum = [0] * (N+1)

for i in range(N):
    prefix_sum[i+1] = prefix_sum[i] + A_list[i]

for _ in range(Q):
    B = int(input())
    # output = sum(A (A<B)) + sum(B-1 (A>-B)) + 1
    if A_list[-1] < B:
        print(-1)
        continue
    idx = bisect.bisect_left(A_list,B)
    output = prefix_sum[idx] + (B-1)*(N-idx) + 1
    print(output)