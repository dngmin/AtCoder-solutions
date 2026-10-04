X = int(input())
happiness = 0

coin_500 = X // 500
happiness += coin_500 * 1000
X -= coin_500 * 500

coin_5 = X // 5
happiness += coin_5 * 5

print(happiness)