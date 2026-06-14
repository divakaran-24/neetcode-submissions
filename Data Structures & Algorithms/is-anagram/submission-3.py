class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS,countT = {},{}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(0,s[i])
            countT[s[i]] = 1 + countT.get(0,t[i])


        for c in countS:
            if countS[c] != countT.get(0,c):
                return False
            
        return True

        
        
        