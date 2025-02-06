# Sudoku Solver

This project is a **Sudoku puzzle generator and solver** implemented in Python. It generates a random Sudoku puzzle and attempts to solve it using a heuristic-based approach. Its really fast and I'm really proud for that.

## Files
- **`main.py`**: The main script that contains the functions for generating, printing, and solving Sudoku puzzles.

## Functions
### `create_puzzle()`
Generates a random Sudoku puzzle with some cells removed.

### `print_puzzle(puzzle)`
Prints the Sudoku puzzle in a readable format.

### `is_solved(puzzle)`
Checks if the Sudoku puzzle is solved.

### `check_collisions(puzzle, i, j, val)`
Checks the number of collisions for a given value in a specific cell.

### `distance_error(puzzle)`
Returns the cell with the most number of collisions.

### `potential_solutions(puzzle, index)`
Returns a list of numbers that can be placed in a specific cell without causing collisions.

### `sudoku_solver(puzzle)`
Solves the Sudoku puzzle using a heuristic-based approach.

## Usage
To run the project, execute the `main.py` script:
```bash
python main.py
```

The script will:
1. Generate a random Sudoku puzzle.
2. Print the initial puzzle.
3. Solve the puzzle.
4. Print the solved puzzle.

---

Enjoy solving Sudoku puzzles with Python! 🎯