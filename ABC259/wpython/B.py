import math
a, b, d = map(int,input().split())
if a == 0 and b == 0:
    print(0, 0)
else:
    r = math.sqrt(a*a + b*b)
    theta = math.atan2(b, a) + math.pi * d / 180
    print(r*math.cos(theta), r*math.sin(theta))