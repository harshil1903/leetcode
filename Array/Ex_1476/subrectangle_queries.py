class SubrectangleQueries:
    def __init__(self, rectangle):
        self.r = rectangle

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        for i in range(row1, row2+1):
            for j in range(col1, col2+1):
                self.r[i][j] = newValue


    def getValue(self, row: int, col: int) -> int:
        return int(self.r[row][col])

if __name__ == '__main__':
    subrectangleQueries = SubrectangleQueries([[1, 2, 1], [4, 3, 4], [3, 2, 1], [1, 1, 1]]);

    print(subrectangleQueries.getValue(0, 2))
    subrectangleQueries.updateSubrectangle(0, 0, 3, 2, 5);
    print(subrectangleQueries.getValue(0, 2))
    print(subrectangleQueries.getValue(3, 1))
    subrectangleQueries.updateSubrectangle(3, 0, 3, 2, 10);
    print(subrectangleQueries.getValue(3, 1))
    print(subrectangleQueries.getValue(0, 2))

