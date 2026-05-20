class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        subset = []
        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return 

            # with include the number
            subset.append(nums[i])
            dfs(i+1)


            #without including that number

            subset.pop()
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            
            dfs(i+1)

        dfs(0)
        return res




