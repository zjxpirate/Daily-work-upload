
import math, collections

list1 = [[1, 3, 4, 2], [3, 1, 2, 4], [1, 4, 3, 2], [4, 3, 2, 1]]

# Check if a partially filled matrix has any conflicts.

def is_valid_sudoku(partial_assignment):

    # Return true if subarray
    # [artial_assignment[start_row : end_row][start_col : end_col]
    # duplicates in {1, 2, ......, len(partial_assignment)}; other wise return False.
    def has_duplicate(block):
        block = list(filter(lambda x: x != 0, block))
        return len(block) != len(set(block))

    n = len(partial_assignment)
    # Check row and column constraints.
    if any(has_duplicate([partial_assignment[i][j] for j in range(n)]) or has_duplicate([partial_assignment[j][i] for j in range(n)]) for i in range(n)):
        return False


    # Check region constraints.
    region_size = int(math.sqrt(n))
    return all(not has_duplicate([partial_assignment[a][b] for a in range(region_size * I, region_size * (I + 1)) for b in range(region_size * J, region_size * (J + 1))]) for I in range(region_size) for J in range(region_size))



# Pythonic solution that exploits the power of list comprehension.

def is_valid_sudoku_pythonic(partial_assignment):
    region_size = int(math.sqrt(len(partial_assignment)))
    return max(collections.Counter(k for i, row in enumerate(partial_assignment) for j, c in enumerate(row) if c != 0 for k in ((i, str(c)), (str(c), j), (i / region_size, j / region_size, str(c)))).values(), default = 0) <= 1



result = is_valid_sudoku(list1)
print(result)



