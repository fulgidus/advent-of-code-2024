def count_XMAS(grid):
    # Check if the grid is empty
    if not grid or not grid[0]:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    directions = [
        (-1, 0),   # Up
        (1, 0),    # Down
        (0, -1),   # Left
        (0, 1),    # Right
        (-1, -1),  # Up-Left
        (-1, 1),   # Up-Right
        (1, -1),   # Down-Left
        (1, 1)     # Down-Right
    ]
    count = 0

    def is_valid(x, y):
        # Check if the coordinates are within the grid boundaries
        return 0 <= x < rows and 0 <= y < cols

    def check_direction(x, y, dr, dc):
        sequence = []
        for _ in range(4):
            if not is_valid(x, y):
                return 0
            sequence.append(grid[x][y])
            x += dr
            y += dc
        if ''.join(sequence) == "XMAS":
            return 1
        return 0

    for start_row in range(rows):
        for start_col in range(cols):
            for dr, dc in directions:
                count += check_direction(start_row, start_col, dr, dc)
    return count

def count_xmas_trees(matrix, rows, cols):
    count = 0
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            # Check the diagonals around position (i, j)
            diag1 = [matrix[i - 1][j - 1], matrix[i][j], matrix[i + 1][j + 1]]
            diag2 = [matrix[i - 1][j + 1], matrix[i][j], matrix[i + 1][j - 1]]
            valid_diag1 = diag1 == ['M', 'A', 'S'] or diag1 == ['S', 'A', 'M']
            valid_diag2 = diag2 == ['M', 'A', 'S'] or diag2 == ['S', 'A', 'M']
            if valid_diag1 and valid_diag2:
                count += 1
    return count

def read_input_from_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        rows = len(lines)
        cols = len(lines[0].strip())
    grid = [line.strip() for line in lines]
    return grid, rows, cols
# Example usage
file_path = 'day4.txt'
grid, rows, cols = read_input_from_file(file_path)
occurrences = count_XMAS(grid)  # Output should be the number of "XMAS" sequences found
occurrences2 = count_xmas_trees(grid, rows, cols)  # Output should be the number of X-'MAS' trees found
print(f"The word 'XMAS' appears {occurrences} times in the grid.")
print(f"The X-'MAS' appears {occurrences2} times in the grid.")