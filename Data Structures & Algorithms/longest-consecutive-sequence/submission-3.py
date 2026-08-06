class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        longest = 0
        if not nums:
            return -1

        numSet = set(nums)
        for num in nums:
            if num-1 not in numSet:
                current = num
                lenght = 1

                while current + 1 in numSet:
                    current += 1
                    lenght += 1
                longest = max(longest,lenght)
        return longest


        