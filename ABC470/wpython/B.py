N = int(input())
C_list = list(map(int,input().split()))
C_count = {}
for C in C_list:
    try:
        C_count[C] += 1
    except:
        C_count[C] = 1
print(N - max(C_count.values()))