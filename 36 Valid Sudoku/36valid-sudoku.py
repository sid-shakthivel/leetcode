class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            row_set = set()
            col_set = set()

            for col in range(9):
                if board[row][col] != ".":
                    if board[row][col] in row_set:
                        # print("Failed at row")
                        return False
                    row_set.add(board[row][col])

                if board[col][row] != ".":
                    if board[col][row] in col_set:
                        # print("Failed at col")
                        return False
                    col_set.add(board[col][row])

        for box_row in range(3):
            for box_col in range(3):
                
                box_set = set()

                for row in range(3):
                    for col in range(3):
                        element = board[box_row * 3 + row][box_col *3 + col]
                        if element != ".":
                            if element in box_set:
                                # print("Failed at box")
                                return False  

                            box_set.add(element)

        return True
                