class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        """
        Find the repeated and missing values in an n×n grid using mathematical approach.

        Time Complexity: O(n²) - single pass through the grid
        Space Complexity: O(1) - uses constant extra space

        Args:
            grid: n×n grid containing numbers from 1 to n²
                with one number repeated and one number missing

        Returns:
            List containing [repeated_value, missing_value]
        """
        # Get grid dimensions
        n = len(grid)
        n_squared = n * n

        # Calculate actual sums from grid
        actual_sum = sum(num for row in grid for num in row)
        actual_square_sum = sum(num ** 2 for row in grid for num in row)

        # Calculate expected sums for numbers 1 to n²
        expected_sum = n_squared * (n_squared + 1) // 2
        expected_square_sum = n_squared * (n_squared + 1) * (2 * n_squared + 1) // 6

        # Calculate differences
        # If x is repeated and y is missing:
        # sum_diff = x - y
        # square_diff = x² - y² = (x-y)(x+y)
        sum_diff = actual_sum - expected_sum
        square_diff = actual_square_sum - expected_square_sum

        # Solve for x and y
        # From square_diff = (x-y)(x+y), we get (x+y) = square_diff / sum_diff
        # Using sum_diff = x - y and x+y = square_diff / sum_diff, we can find x and y
        x_plus_y = square_diff // sum_diff

        repeated = (x_plus_y + sum_diff) // 2
        missing = (x_plus_y - sum_diff) // 2

        return [repeated, missing]
