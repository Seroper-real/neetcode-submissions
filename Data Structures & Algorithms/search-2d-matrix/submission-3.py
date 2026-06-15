class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rid = len(matrix) * len(matrix[0]) - 1
        return self.b_search(matrix, target, 0, rid)
        

    def get_linear(self, matrix: List[List[int]], index: int) -> int:
        n = len(matrix[0])
        return matrix[index // n][index % n]

    def b_search(self, matrix: List[List[int]], target: int, lid: int, rid: int) -> bool:
        if rid - lid <= 1:
            v1 = self.get_linear(matrix, lid)
            v2 = self.get_linear(matrix, rid)
            return target == v1 or target == v2
        idx = lid + ((rid - lid) // 2)
        #print(f"lid:{lid}, rid:{rid}, idx:{idx}")
        val = self.get_linear(matrix, idx)
        if val == target: return True
        elif val > target: return self.b_search(matrix, target, lid, idx)
        elif val < target: return self.b_search(matrix, target, idx, rid)
