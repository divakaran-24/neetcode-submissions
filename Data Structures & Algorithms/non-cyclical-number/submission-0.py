class Solution:
    def sumofdigits(self,n):
        total = 0
        while n!=0:
            num = n%10
            total += num*num
            n = n // 10
        return total
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n!=1:
            if n in seen:
                return False
            
            seen.add(n)
            n = self.sumofdigits(n)
        return True


            

   
            

        

        