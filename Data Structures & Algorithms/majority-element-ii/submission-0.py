class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ele = 0
        ele2 = 0
        cnt1 = 0
        cnt2 = 0
        for num in nums:
            if num == ele:
                cnt1 += 1
            elif num == ele2:
                cnt2 += 1
            elif cnt1 == 0:
                ele = num
                cnt1 += 1
            elif cnt2 == 0:
                ele2 = num
                cnt2 += 1
            else:
                cnt1 -= 1
                cnt2 -= 1
        cnt1 = 0
        cnt2 = 0
        for num in nums:
            if num == ele:
                cnt1 += 1
            if num == ele2:
                cnt2 += 1
        ans = []
        if cnt1 > len(nums) // 3:
            ans.append(ele)

        if cnt2 > len(nums) // 3:
            ans.append(ele2)

        return ans
            
        


        