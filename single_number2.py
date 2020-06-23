from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        c = Counter(nums)
        for k in c:
            if c[k] == 1:
                return k