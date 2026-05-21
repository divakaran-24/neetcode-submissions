class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        lenght = sum(matchsticks) // 4
        sides = [0] * 4
        if sum(matchsticks) / 4 != lenght:
            return False
        
        def bt(i):
            if i >= len(matchsticks):
                return True
            
            for j in range(4):
                if sides[j] + matchsticks[i] <= lenght:
                    sides[j] += matchsticks[i]
                    if bt(i+1):
                        return True
                    sides[j] -= matchsticks[i]
            return False
        return bt(0)

                
        