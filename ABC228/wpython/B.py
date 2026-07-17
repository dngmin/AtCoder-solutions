N, X = map(int,input().split())
A_list = list(map(int,input().split()))
know = [False]* (N+1)
output = 0
while not know[X]:
    know[X] = True
    X = A_list[X-1]
    output += 1
print(output)