p, q = input().split()
diff = [0, 3, 4, 8, 9, 14, 23]
alph = ["A","B","C","D","E","F","G"]
print(abs(diff[alph.index(p)] - diff[alph.index(q)]))