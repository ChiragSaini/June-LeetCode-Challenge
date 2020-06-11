class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ### First Soln 76ms
#         zeros = 0
#         ones = 0
#         twos = 0
#         for color in nums:
#             if color == 0:
#                 zeros += 1
#             elif color == 1:
#                 ones += 1
#             elif color == 2:
#                 twos += 1
        
#         for i in range(len(nums)):
#             if zeros > 0:
#                 nums[i] = 0
#                 zeros -= 1
#             elif ones > 0:
#                 nums[i] = 1
#                 ones -= 1
#             else:
#                 nums[i] = 2
#                 twos -= 1
#         return nums
        ### Second Solution
        n0, n1, n2 = 0, 0, 0
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[n2] = 2
                nums[n1] = 1
                nums[n0] = 0
                n2 += 1
                n1 += 1
                n0 += 1
            elif nums[i] == 1:
                nums[n2] = 2
                nums[n1] = 1
                n2 += 1
                n1 += 1
            elif nums[i] == 2:
                nums[n2] = 2
                n2 += 1
        return nums