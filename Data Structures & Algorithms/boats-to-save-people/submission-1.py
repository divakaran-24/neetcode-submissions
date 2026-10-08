class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        count1 = 0
        people.sort()
        n = len(people)
        l,r = 0,n-1
        while l <= r:
            sum1 = people[l] + people[r]
            if sum1 <= limit:
                l+=1
            r -= 1
            count1 += 1
        return count1

        