class Solution:
        def maxProduct(self, nums: List[int]) -> int:
                res = max(nums)
                currmax , currmin = 1,1
                for n in nums:
                        if n == 0:
                                continue

                        tmp = n*currmax
                        currmax = max(n*currmax,n*currmin,n)
                        currmin = min(tmp,n*currmin,n)

                res = max(res,currmax)

                return res 

                        
        
                        
                            