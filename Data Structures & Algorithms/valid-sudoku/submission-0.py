class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        buckets = defaultdict(list)
        for i in range(len(board)):
            seen_row = set()
            seen_col = set()
            for j in range(len(board)):
                val_row = board[i][j]
                if val_row != '.':
                    if val_row in seen_row: return False
                    seen_row.add(val_row)
                    bucket = ((i // 3) * 3) + (j // 3)
                    if val_row in buckets[bucket]: return False
                    buckets[bucket].append(val_row)
                val_col = board[j][i]
                if val_col != '.':
                    if val_col in seen_col: return False
                    seen_col.add(val_col)
        return True