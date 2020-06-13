class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        if n == 0:
            return []
        dp = [ [nums[i]] for i in range(n)]
        answer = [nums[0]]
        for i in range(1, n):
            for j in range(0, i):
                if nums[i] % nums[j] == 0:
                    t = dp[j] + [nums[i]]
                    if len(t) > len(dp[i]):
                        dp[i] = list(t)
                    if len(dp[i]) > len(answer):
                        answer = dp[i]
        return answer