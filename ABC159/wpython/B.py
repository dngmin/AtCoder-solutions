S = input()
N = len(S)
def check_Palindrome(input):
    size = len(input)
    if size % 2 == 0:
        return input[:size//2] == input[size//2:][::-1]
    else:
        return input[:size//2 + 1] == input[size//2:][::-1]

Palindrome = check_Palindrome(S) & check_Palindrome(S[:(N-1)//2]) & check_Palindrome(S[(N+3)//2-1:])
print("Yes" if Palindrome else "No")