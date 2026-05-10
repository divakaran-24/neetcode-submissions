class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ""
        for n in s:
            if n.isalnum():
                res+=n.lower()
        if res == res[::-1]:
            return True
        
        return False
        


        