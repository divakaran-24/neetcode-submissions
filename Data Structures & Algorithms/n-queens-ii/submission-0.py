class Solution:
    def totalNQueens(self, n: int) -> int:
        posDig = set()
        negDig = set()
        col = set()

        res = 0
        def bt(r):
            if r == n:
                nonlocal res
                res += 1
                return 

            for c in range(n):
                if c in col or (r+c) in posDig or (r-c) in negDig:
                    continue

                posDig.add(r+c)
                negDig.add(r-c)
                col.add(c)

                bt(r+1)

                posDig.remove(r+c) 
                negDig.remove(r-c)
                col.remove(c)

        bt(0)
        return res



        