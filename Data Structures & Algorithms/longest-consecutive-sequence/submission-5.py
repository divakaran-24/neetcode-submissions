class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        seen = set(nums)
        lenght = 0
        longest = 0
        if not nums:
            return 0
        for num in nums:
            if num-1 not in seen:
                current = num
                lenght = 1
            
                while current+1 in seen:
                    current += 1
                    lenght += 1
                longest = max(longest,lenght)

        return longest


