A, B = map(int,input().split())
print((A*A - B*B) // (2*(A-B)) if (A*A - B*B) % (2*(A-B)) == 0 else "IMPOSSIBLE")