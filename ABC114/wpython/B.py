S = input()
minimum = 999
for i in range(len(S)-2):
    minimum = min(abs(753 - int(S[i:i+3])), minimum)
print(minimum)