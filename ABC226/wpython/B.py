N = int(input())
lists = set()
for _ in range(N):
    l = input()
    lists.add(l[l.find(" ")+1:])
print(len(lists))