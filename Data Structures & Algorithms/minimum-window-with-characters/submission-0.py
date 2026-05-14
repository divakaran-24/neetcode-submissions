class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        s1count = {}
        window = {}
        
        for c in t:
            s1count[c] = s1count.get(c,0) + 1

        have , need = 0 , len(s1count)

        res = [-1,-1]
        reslen = float("inf")

        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c,0) + 1
           
            if c in s1count and window[c] == s1count[c]:
                have += 1
                
            
            while have == need:
                if (r - l + 1) < reslen:
                    res = [l,r]
                    reslen = r - l + 1
                
                window[s[l]] -= 1
                if s[l] in s1count and window[s[l]] < s1count[s[l]]:
                    have -= 1
                
                l += 1
        
        l,r = res
        return s[l:r+1] if reslen != float("inf") else ""




        
        