FizzBuzz_sum = 0
for i in range(1,int(input())+1):
    FizzBuzz_sum += 0 if i % 3 == 0 or i % 5 == 0 else i
print(FizzBuzz_sum)