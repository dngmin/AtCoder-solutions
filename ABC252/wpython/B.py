N, K = map(int,input().split())
A_list = list(map(int,input().split()))
B_list = list(map(int,input().split()))
hate = False
tasty = 0
for i, A in enumerate(A_list, start = 1):
    if A > tasty:
        tasty = A
        hate = True if i in B_list else False
    elif  A == tasty and i in B_list:
        hate = True
print("Yes" if hate else "No")