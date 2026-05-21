class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        per = []
        count = {}
        for n in nums:
            count[n] = count.get(n,0)+1

        def dfs():

            if(len(nums) == len(per)):
                res.append(per.copy())
            
            for n in count:
                if count[n] > 0:
                    per.append(n)
                    count[n] -= 1
                    dfs()

                    count[n] += 1
                    per.pop()
            
        dfs()
        return res
                




        