abc = int(input())
a, b, c, = abc//100, (abc//10)%10, abc%10
abc = a+b+c
print(abc*100 + abc*10 + abc)