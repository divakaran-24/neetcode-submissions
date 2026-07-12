class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in  nums:
            count[num] = 1 + count.get(0,num) 

        freq = [[] for _ in range(len(count)+1)]

        for num,frq in count.items():
            freq[frq].append(num)

        res = []
        for i in range(len(freq)-1,0,-1):
            for num in freq[i]:
                res.append(num)

                if (len(res) == k):
                    return res
            



        