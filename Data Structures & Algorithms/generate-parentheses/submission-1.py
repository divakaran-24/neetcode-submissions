class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def bt(s,op,cl):
            if len(s) == n*2:
                res.append(s)
            if op < n:
                bt(s+'(',op+1,cl)
            if cl < n and op>cl:
                bt(s+')',op,cl+1)
        bt("",0,0)
        return res 


            