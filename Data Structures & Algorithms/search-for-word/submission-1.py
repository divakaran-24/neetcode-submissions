class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows , cols = len(board),len(board[0])
        res = []
        pos = set()
        def dfs(r,c,i):
            if len(word) == i:
                return True
            
            if (r < 0 or c < 0 or word[i] != board[r][c] or (r,c) in pos):
                return False
            pos.add((r,c))
            res = (dfs(r+1,c,i+1) or dfs(r-1,c,i+1) or dfs(r,c+1,i+1) or dfs(r,c-1,i+1))
            pos.remove((r,c))
            return res

        for r in range(rows):
            for c in range(cols):
                if dfs(r,c,0):
                    return True
        
        return False

        