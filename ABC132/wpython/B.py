n = int(input())
p = list(map(int,input().split()))
count = 0
for i in range(n-2):
    list_p123 = [p[i],p[i+1],p[i+2]]
    count += (sum(list_p123) - max(list_p123) - min(list_p123)) == p[i+1]
print(count)