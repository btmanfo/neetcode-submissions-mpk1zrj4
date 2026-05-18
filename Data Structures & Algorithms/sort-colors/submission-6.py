class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return None
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
        trackOne = 0
        while trackOne< len(nums) and nums[trackOne] == 0:
            trackOne +=1
        print(trackOne)    
        for i in range(trackOne, len(nums)):
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
                        j = len(nums)
                    else:
                        j+=1