import random
import copy

def create_puzzle():
    puzzle = [[0 for x in range(9)] for y in range(9)]
    #creating an initially solved puzzle
    for i in range(9):
        for j in range(9):
            puzzle[i][j] = (i * 3 + i // 3 + j) % 9 + 1
    #randomly exchanging digits in the board random number of times
    for i in range(random.randint(1, 100)):
        d1 = random.randint(1, 9)
        d2 = random.randint(1, 9)
        for i in range(9):
            for j in range(9):
                if puzzle[i][j] == d1:
                    puzzle[i][j] = d2
                elif puzzle[i][j] == d2:
                    puzzle[i][j] = d1
    #exchanging edge rows in same block if rand is true
    if random.randint(0, 1) == 1:
        for i in range(3):
            for j in range(9):
                puzzle[i][j], puzzle[i + 3][j] = puzzle[i + 3][j], puzzle[i][j]
    #exchanging edge columns in same block if rand is true
    if random.randint(0, 1) == 1:
        for i in range(3):
            for j in range(9):
                puzzle[j][i], puzzle[j][i + 3] = puzzle[j][i + 3], puzzle[j][i]
    #removing 50% values from the board
    for i in range(9):
        for j in range(9):
            if random.randint(0, 1) == 1:
                puzzle[i][j] = 0
    return puzzle

def print_puzzle(puzzle):
    for i in range(9):
        for j in range(9):
            print(puzzle[i][j], end = " ")
        print()

def is_solved(puzzle):
    #checking if all rows and columns are valid
    for i in range(9):
        sum = 0
        for j in range(9):
            sum += puzzle[j][i] + puzzle[i][j]
        if sum != 90:
            return False
    #checking if all blocks are valid
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            sum = 0
            for k in range(3):
                for l in range(3):
                    sum += puzzle[i + k][j + l]
            if sum != 45:
                return False
    return True

#check number of collisions for val in the cell
def check_collisions(puzzle, i, j, val):
    distance = 0
    #check if val is not repeating in the row
    for l in range(9):
        if puzzle[i][l] == val:
            distance += 1
    #check if val is not repeating in the column
    for l in range(9):
        if puzzle[l][j] == val:
            distance += 1
    #check if val is not repeating in the block
    for l in range(3):
        for m in range(3):
            if puzzle[i - i % 3 + l][j - j % 3 + m] == val:
                distance += 1
    return distance


#Return the cell with the most number of collisions
def distance_error(puzzle):
    max_distance = -1
    index = [-1, -1]
    for i in range(9):
        for j in range(9):
            distance = 0
            if puzzle[i][j] != 0:
                continue
            #puzzle[i][j] is empty
            for k in range(1, 10):
                distance += check_collisions(puzzle, i, j, k)
            if distance > max_distance:
                max_distance = distance
                index = [i, j]
    return index

#Function returns list of numbers that can be placed in the cell
def potential_solutions(puzzle, index):
    index_i = index[0]
    index_j = index[1]
    solutions = []
    for k in range(1, 10):
        if (check_collisions(puzzle, index_i, index_j, k) == 0):
            solutions.append(k)
    return solutions

def suduko_solver(puzzle):
    iterations = 0
    open = [puzzle]
    closed = []
    if (is_solved(puzzle)):
        print("Puzzle is already solved!")
        print ("Numer of Iterations: ", iterations)
        return puzzle
    while True:
        node = open.pop()
        if (is_solved(node)):
            print("Puzzle solved!")
            print("Number of Iterations: ", iterations)
            return node
        #Heuristics: Number of collisions in the cell
        index = distance_error(node)
        if (index[0] == -1):
            continue
        iterations += 1
        #Check all solutions in the cell
        solutions = potential_solutions(node, index)
        # UNCOMMENT THIS TO SEE WHICH INDEXES ARE BEING CHANGED
        # print("Potential solutions: ", solutions)
        # print("Index: ", index)
        for i in range(len(solutions)):
            temp = copy.deepcopy(node)
            temp[index[0]][index[1]] = solutions[i]
            open.append(temp)
        if (not node):
            print("No solution found!")
            return None
        
# puzzle_given = [[0,6,0,1,0,4,0,5,0], 
#        [0,0,8,3,0,5,6,0,0], 
#        [2,0,0,0,0,0,0,0,1],
#        [8,0,0,4,0,7,0,0,6],
#        [0,0,6,0,0,0,3,0,0],
#        [7,0,0,9,0,1,0,0,4],
#        [5,0,0,0,0,0,0,0,2],
#        [0,0,7,2,0,6,9,0,0],
#        [0,4,0,5,0,8,0,7,0]]     

#Main
print("Puzzle:")
puzzle = create_puzzle()
print_puzzle(puzzle)
print()
print("Solved Puzzle:")
puzzle = suduko_solver(puzzle)
print_puzzle(puzzle)