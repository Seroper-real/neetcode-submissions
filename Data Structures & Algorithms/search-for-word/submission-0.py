class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        store = set()
        word_list = list(word)
        
        def search(word_idx: int, row: int, col: int) -> bool:
            if word_idx >= len(word_list):
                return True

            moves = []
            if row > 0: moves.append((row-1, col)) #UP
            if row < len(board)-1: moves.append((row+1, col)) #DOWN
            if col > 0: moves.append((row, col-1)) #LEFT
            if col < len(board[row])-1: moves.append((row, col+1)) #RIGHT

            for (i, j) in moves:
                #print(f"MOVE - {i},{j},{word_idx}")
                if (i, j) in store: continue
                if board[i][j] == word_list[word_idx]:
                    #print(f"INNER - {i},{j}:{board[i][j]} == {word_list[word_idx]}")
                    store.add((i, j))
                    word_idx += 1
                    if search(word_idx, i, j): return True
                    store.remove((i, j))
                    word_idx -= 1
            return False

        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == word_list[0]:
                    #print(f"OUTER - {row},{col}:{board[row][col]} == {word_list[0]}")
                    store.add((row, col))
                    if search(1, row,col): return True
                    store.remove((row, col))
        return False
        
