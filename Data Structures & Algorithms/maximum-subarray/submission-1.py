class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi = float('-inf')
        sum1 = 0
        for num in nums:
            sum1 += num
            if sum1 > maxi:
                maxi = sum1
            if sum1 < 0:
                sum1 = 0
        return maxi
            
            
        