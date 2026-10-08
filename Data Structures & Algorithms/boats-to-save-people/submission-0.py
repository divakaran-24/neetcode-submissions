class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        res = 0
        count1 = 0
        for i in range(len(people)):
            if people[i] == limit:
                count1+=1
            else:
                for j in range(i+1,len(people)):
                    if people[i] + people[j] == limit:
                        count1 += 1
        return count1

        