class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        currMax=0
        currMin=0
        best =nums[0]
        lowest = nums[0]
        total =0

        for num in nums:
            currMax = max(currMax+num,num)
            currMin = min(currMin+num, num)
            total+=num
            best = max(currMax,best)
            lowest = min(currMin,lowest)
        
        return max(best,total-lowest) if best > 0 else best


