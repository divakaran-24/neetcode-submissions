class Solution:
    def trap(self, height: List[int]) -> int:
        res = [0] * len(height)
        leng = len(height)
        maxl = height[0]
        maxr = height[leng - 1]
        l , r = 0 , leng - 1
        while l < r :
            if maxl <= maxr:
                l += 1
                newval = maxl - height[l]

                if (newval) > 0:
                    res[l] = newval
                
                maxl = max(height[l],maxl)
            else:
                r -= 1
                newval = maxr - height[r]
                if (newval) > 0:
                    res[r] =  newval
                
                maxr = max(height[r],maxr)
        
        res_sum = sum(res)
        return res_sum
    




        