class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        posDig = set()
        negDig = set()
        col = set()

        board = [["."]*n for i in range(n)]

        def bt(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return 
            
            for c in range(n):
                if c in col or (r+c) in posDig or (r-c) in negDig:
                    continue
                posDig.add(r+c)
                negDig.add(r-c)
                col.add(c)
                board[r][c] = "Q"
                bt(r+1)

                posDig.remove(r+c)
                negDig.remove(r-c)
                col.remove(c)
                board[r][c] = "."
        
        bt(0)
        return res




        