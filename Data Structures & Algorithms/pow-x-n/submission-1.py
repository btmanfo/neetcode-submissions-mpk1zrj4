class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n ==1:
            return x
        if n == 0:
            return 1
        if n > 0:
            res = x
            for i in range(1, n):
                res = res * x
            return res
        else:
            res = 1/x
            for i in range(1, -n):
                res = res *1/x
            return res