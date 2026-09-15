from enum import Enum


class Direction(Enum):
    UP = 'UP'
    DOWN = 'DOWN'
    LEFT = 'LEFT'
    RIGHT = 'RIGHT'

class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        elements = []

        i = 0
        j = 0

        width = len(matrix[0])
        height = len(matrix)

        top = 1
        bottom = height - 1
        left = 0
        right = width - 1

        currentDirection = Direction.RIGHT

        def getNextDirection(direction):
            if direction == Direction.UP:
                return Direction.RIGHT
            elif direction == Direction.DOWN:
                return Direction.LEFT
            elif direction == Direction.LEFT:
                return Direction.UP
            else:
                # If RIGHT go DOWN
                return Direction.DOWN

        while len(elements) < width * height:
            if currentDirection == Direction.RIGHT:
                while j <= right:
                    elements.append(matrix[i][j])
                    j += 1

                right -= 1
                j -= 1
                i += 1
            elif currentDirection == Direction.DOWN:
                while i <= bottom:
                    elements.append(matrix[i][j])
                    i += 1
                
                bottom -= 1
                i -= 1
                j -= 1
            elif currentDirection == Direction.LEFT:
                while j >= left:
                    elements.append(matrix[i][j])
                    j -= 1
                
                left += 1
                i -= 1
                j += 1
            else:
                while i >= top:
                    print(f"adding {matrix[i][j]}")
                    elements.append(matrix[i][j])
                    i -= 1
                
                top += 1
                i += 1
                j += 1

            currentDirection = getNextDirection(currentDirection)

        return elements