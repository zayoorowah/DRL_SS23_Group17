def print_grid(grid):
    # Print the top border
    print("+" + "-" * (len(grid[0]) * 2 + 1) + "+")
    # Print each row
    for row in grid[::-1]:
        # Print the left border
        print("|", end="")
        # Print each cell
        for cell in row:
            # Print the cell value
            print(" " + str(cell), end="")
        # Print the right border
        print(" |")
    # Print the bottom border
    print("+" + "-" * (len(grid[0]) * 2 + 1) + "+")
