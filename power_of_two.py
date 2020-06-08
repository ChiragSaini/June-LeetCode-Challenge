class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1 or n == 2:
            return True
        if n <= 0:
            return False
        while n > 1:
            if n%2 != 0:
                return False
            temp = n / 2
            if temp%2 != 0 and temp != 1:
                return False
            n = n / 2
            print(n)
        return True