class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if board is None:
            return False
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)
        for i in range(0,9):
            for j,v in enumerate(board[i]):
                if board[i][j].isdigit() and int(board[i][j])<=9 and int(board[i][j])>=1:
                    if v in rows[i] or v in cols[j] or v in squares[(i//3,j//3)]:
                        return False
                    else:
                        rows[i].add(v)
                        cols[j].add(v)
                        squares[(i//3,j//3)].add(v)
        return True