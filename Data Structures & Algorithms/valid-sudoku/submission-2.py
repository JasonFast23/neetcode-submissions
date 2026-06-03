class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()

        for row in range (9):
            for col in range(9):
                value = board[row][col]

                if value == ".":
                    continue

                row_key = (value, "row", row)
                col_key = (value, "col", col)
                box_key = (value, "box", row // 3, col // 3)

                if row_key in seen or col_key in seen or box_key in seen:
                    return False

                seen.add(row_key)
                seen.add(col_key)
                seen.add(box_key)

        return True