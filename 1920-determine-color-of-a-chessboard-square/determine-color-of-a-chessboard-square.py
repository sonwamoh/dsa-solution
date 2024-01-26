class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        x_axis = ord(coordinates[0]) - 96
        y_axis = int(coordinates[1])
        return (x_axis + y_axis) % 2 == 1

        