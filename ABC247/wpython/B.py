N = int(input())
s, t = [], []
for _ in range(N):
    st = input().split()
    s.append(st[0])
    t.append(st[1])
for i in range(N):
    S, T = s[i], t[i]
    s_posible = True
    t_posible = True
    for j in range(N):
        if i == j:
            continue
        if (S == s[j] or S == t[j]):
            s_posible = False
        if (T == s[j] or T == t[j]):
            t_posible = False
        if not s_posible and not t_posible:
            print("No")
            exit()
print("Yes")