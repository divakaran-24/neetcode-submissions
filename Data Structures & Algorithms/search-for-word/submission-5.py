class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)-1
        col = len(board[0])-1
        def bt(i,r,c):
            if i==len(word):
                return True
            if r < 0 and c < 0 and r >= row and c >= col:
                return 
            if word[i] != board[r][c]:
                return False
            temp = board[r][c]
            board[r][c] = '#'
            found = (bt(i+1,r+1,c) or bt(i+1,r-1,c) or bt(i+1,r,c+1) or bt(i+1,r,c-1))
            board[r][c] = temp
            return found
        for r in range(row):
            for c in range(col):
                if word[0] == board[r][c]:
                    if bt(0,r,c):
                        return True

        return False


        