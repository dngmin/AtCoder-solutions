S1S2 = input()
T1T2 = input()
point = {'A' : ['B','E'],
         'B' : ['A','C'],
         'C' : ['B','D'],
         'D' : ['C','E'],
         'E' : ['D','A']}
if S1S2[1] in point[S1S2[0]]:
    print("Yes" if T1T2[1] in point[T1T2[0]] else "No")
else:
    print("No" if T1T2[1] in point[T1T2[0]] else "Yes")