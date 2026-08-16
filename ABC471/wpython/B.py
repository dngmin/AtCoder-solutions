N = int(input())
S_dict = dict()
for _ in range(N):
    S = input().lower()
    try:
        S_dict[S] += 1
    except:
        S_dict[S] = 1
print(max(S_dict.values()))