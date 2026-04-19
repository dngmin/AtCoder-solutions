N, M = map(int,input().split())
F_len = len(set(map(int,input().split())))

print("Yes" if F_len == N else "No")
print("Yes" if F_len == M else "No")