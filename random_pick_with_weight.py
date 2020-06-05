
# !  Found his problem really hard to understand in beginning
class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        # Part of Brute Force Approach
        # self.n = len(self.w)
        # self.r = []
        # for i, weight in enumerate(self.w):
        #     for j in range(weight):
        #         self.r.append(i)
        ## Approach 2
        self.c = []
        temp =0
        for weight in self.w:
            temp += weight
            self.c.append(temp)
                
    def pickIndex(self) -> int:
        # TLE on Brute Force
        # return random.choice(self.r)
        ## Approach 2
        rand = random.randint(0, self.c[-1])
        l, r = 0, len(self.c)-1
        while l < r:
            m = (l+r) // 2
            if self.c[m] <= rand:
                l = m+1
            else:
                r = m
        return l


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()