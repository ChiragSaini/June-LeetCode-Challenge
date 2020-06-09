from collections import defaultdict
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for c in s:
            index = -1
            tmp = len(t)
            for i in range(tmp):
                if t[i] == c:
                    index = i
                    break
            if index == -1:
                return False
            else:
                t = t[index+1:]
        return True