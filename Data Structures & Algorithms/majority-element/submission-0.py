class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        map = {}
        for n in nums:
            map[n] = map.get(n,0)+1
        
        for key,val in map.items():
            if val > len(nums) // 2:
                return key

 