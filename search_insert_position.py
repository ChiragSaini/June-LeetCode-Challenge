########################
# * First Solution
########################
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1
        while low < high:
            mid = (low+high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid-1
            elif nums[mid] < target:
                low = mid+1
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
        return len(nums)
    
########################
# * Second Solution
########################
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # ? Border Cases
        if target > nums[-1]:
            return len(nums)
        if target <= nums[0]:
            return 0
        ############
        # * Binary Search here
        low = 0
        high = len(nums)-1
        while low < high:
            mid = (low+high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid-1
            elif nums[mid] < target:
                low = mid+1
        # * Simple Traversal here
        for i in range(len(nums)):
            if nums[i] >= target:
                return i            