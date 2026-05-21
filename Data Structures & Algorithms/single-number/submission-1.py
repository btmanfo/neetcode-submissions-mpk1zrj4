class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in nums:
            res = res ^i
        return res
        # we can do this because 1111 ^ 1111 get 0000
        # so it kills all value identical