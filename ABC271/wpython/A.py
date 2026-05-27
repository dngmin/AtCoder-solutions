hexadecimal = "0123456789ABCDEF"
N = int(input())
first = hexadecimal[N//16]
last = hexadecimal[N%16]
print(first+last)