class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        tackZero = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                tackZero += 1
                continue
            else:
                j = i +1
                while j < len(nums):
                    if nums[j] == 0:
                        temp = nums[i]
                        nums[i] = nums[j]
                        nums[j] = temp
                        tackZero = j
                        j = len(nums)
                    else:
                        j+=1 
        trackOne = tackZero +1
        if trackOne >= len(nums):
            return None          
        for i in range(tackZero +1, len(nums)):
            if nums[i] == 1:
                trackOne += 1
                continue
            else:
                j = i +1
                while j < len(nums):
                    if nums[j] == 1:
                        temp = nums[i]
                        nums[i] = nums[j]
                        nums[j] = temp
                        trackOne = j
                        j = len(nums)
                    else:
                        j+=1