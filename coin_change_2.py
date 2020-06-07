# amount = 5
# # amount = 100
# coins = [1, 2, 5]
# # coins = [1, 101, 102, 103]
# n = len(coins)

# dp = [[0]*(amount+1) for _ in range(n+1)]

# for i in range(n+1):
#     dp[i][0] = 1
    
# for i in range(1, n+1):
#     for j in range(1, amount+1):
#         print(f"i:{i}, j:{j}")
#         dp[i][j] = dp[i-1][j] + dp[i][j-coins[i-1]]
        
# print(dp[-1][-1])

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0]*(amount+1)
        dp[0] = 1

        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] += dp[i - coin]
        return dp[amount]
    
# * refer this video for one of the best Explanation: "https://youtu.be/jaNZ83Q3QGc"