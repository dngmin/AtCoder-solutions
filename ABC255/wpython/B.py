N, K = map(int,input().split())
A_list = list(map(int,input().split()))
has_light = []
no_light = []
A_index = 0
for i in range(1, N+1):
    X, Y = map(int,input().split())
    if i == A_list[A_index]:
        has_light.append([X,Y])
        if A_index < K-1:
            A_index += 1
    else:
        no_light.append([X,Y])
minimum_power = 0
for no in no_light:
    minimum_length = 0
    for has in has_light:
        length = ((has[0] - no[0])**2 + (has[1] - no[1])**2) ** 0.5
        if not minimum_length or minimum_length > length:
            minimum_length = length
    if not minimum_power or minimum_power < minimum_length:
        minimum_power = minimum_length
print(minimum_power)