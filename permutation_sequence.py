class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        l = []
        #* Factorials
        fact = [0]*n
        fact[0] = 1
        for i in range(1, n):
            fact[i] = i*fact[i-1]
        for i in range(1, n+1):
            l.append(i)
        k -= 1
        s = []
        for i in range(n-1,-1,-1):
            index = k // fact[i]
            s .append(str(l.pop(index)))
            k = k % fact[i]
        return "".join(s)