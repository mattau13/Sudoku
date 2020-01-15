import math
import pygame
import time

pygame.init()

#  Create Window
window = pygame.display.set_mode((900, 900))
pygame.display.set_caption("Sudoku")

sudoku_board = pygame.image.load("images/board.png").convert()
window.blit(sudoku_board, (0, 0))

pygame.display.update()

#  Load Images
white = pygame.image.load("images/white.png").convert_alpha()
green = pygame.image.load("images/green.png").convert_alpha()
red = pygame.image.load("images/red.png").convert_alpha()

one = pygame.image.load("images/1.png").convert_alpha()
two = pygame.image.load("images/2.png").convert_alpha()
three = pygame.image.load("images/3.png").convert_alpha()
four = pygame.image.load("images/4.png").convert_alpha()
five = pygame.image.load("images/5.png").convert_alpha()
six = pygame.image.load("images/6.png").convert_alpha()
seven = pygame.image.load("images/7.png").convert_alpha()
eight = pygame.image.load("images/8.png").convert_alpha()
nine = pygame.image.load("images/9.png").convert_alpha()

one_t = pygame.image.load("images/1t.png").convert_alpha()
two_t = pygame.image.load("images/2t.png").convert_alpha()
three_t = pygame.image.load("images/3t.png").convert_alpha()
four_t = pygame.image.load("images/4t.png").convert_alpha()
five_t = pygame.image.load("images/5t.png").convert_alpha()
six_t = pygame.image.load("images/6t.png").convert_alpha()
seven_t = pygame.image.load("images/7t.png").convert_alpha()
eight_t = pygame.image.load("images/8t.png").convert_alpha()
nine_t = pygame.image.load("images/9t.png").convert_alpha()

#  GUI Logic

#  Finds the first empty space in the given board and returns the location of that position.
def get_pos(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j


#  Converts coordinates into position values
def convert_coord(pos):
    return int(math.floor(pos[0] / 100)), int(math.floor(pos[1] / 100))


#  Sets the value of a specific position in a given board
def set_value(board, pos, val):
    board[pos[0]][pos[1]] = val


#  Transfers correct values from temp to board by comparing temp w/ solved
def transfer_values(temp, board, solved):
    for i in range(9):
        for j in range(9):
            current_pos = pos_to_coord((i, j))

            if temp[i][j] == 0:
                continue

            if board[i][j] == 0 and temp[i][j] == solved[i][j]:
                board[i][j] = temp[i][j]
            else:
                window.blit(red, current_pos)

    pygame.display.update()
    print("updated")

def pos_to_coord(pos):
    return pos[0] * 100, pos[1] * 100


def get_image(board, i, j, key = True):
    if board[i][j] == 1:
        if key:
            return one
        else:
            return one_t
    elif board[i][j] == 2:
        if key:
            return two
        else:
            return two_t
    elif board[i][j] == 3:
        if key:
            return three
        else:
            return three_t
    elif board[i][j] == 4:
        if key:
            return four
        else:
            return four_t
    elif board[i][j] == 5:
        if key:
            return five
        else:
            return five_t
    elif board[i][j] == 6:
        if key:
            return six
        else:
            return six_t
    elif board[i][j] == 7:
        if key:
            return seven
        else:
            return seven_t
    elif board[i][j] == 8:
        if key:
            return eight
        else:
            return eight_t
    elif board[i][j] == 9:
        if key:
            return nine
        else:
            return nine_t
#  Draws board, key = true refers to solid values, whereas key = false refers to temporary values
def draw_board(board, key = True):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                continue
            current_pos = pos_to_coord((i, j))
            window.blit(white, current_pos)
            window.blit(get_image(board, i, j, key), current_pos)
            pygame.display.update()


#  SOLVE LOGIC
def find_empty_loc(board, loc):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                loc[0] = i
                loc[1] = j
                return True
    return False


def in_row(board, row, val):
    for i in range(9):
        if board[row][i] == val:
            return True
    return False


def in_col(board, col, val):
    for i in range(9):
        if board[i][col] == val:
            return True
    return False


def in_box(board, row, col, val):
    for i in range(3):
        for j in range(3):
            if board[i + row][j + col] == val:
                return True
    return False


def is_safe_loc(board, row, col, val):
    return not in_row(board, row, val) and not in_col(board, col, val) and not in_box(board, row - (row % 3), col - (col % 3), val)


def solve(board, live = False):
    loc = [0, 0]

    if not find_empty_loc(board, loc):
        return True

    row = loc[0]
    col = loc[1]

    for val in range(1, 10):
        if is_safe_loc(board, row, col, val):
            board[row][col] = val
            if live:
                draw_board(board)
                print("new frame")
            if solve(board, live):
                return True
            board[row][col] = 0

    return False


if __name__ == '__main__':
    board = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
             [6, 0, 0, 1, 9, 5, 0, 0, 0],
             [0, 9, 8, 0, 0, 0, 0, 6, 0],
             [8, 0, 0, 0, 6, 0, 0, 0, 3],
             [4, 0, 0, 8, 0, 3, 0, 0, 1],
             [7, 0, 0, 0, 2, 0, 0, 0, 6],
             [0, 6, 0, 0, 0, 0, 2, 8, 0],
             [0, 0, 0, 4, 1, 9, 0, 0, 5],
             [0, 0, 0, 0, 8, 0, 0, 7, 9]]

    #  Create Solved Board to Reference
    solved_board = [board[i][:] for i in range(9)]
    solve(solved_board)

    game_over = False
    solved = False
    pos = get_pos(board)

    #  Create Temporary Board to add/remove temporary moves
    temp_board = [[0 for _ in range(9)] for _ in range(9)]

    draw_board(board)

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                #  Transfer Everything from Temp Board to Real Board iff it is correct?
                if event.key == pygame.K_RETURN:
                    transfer_values(temp_board, board, solved_board)
                    temp_board = [[0 for _ in range(9)] for _ in range(9)]
                    draw_board(board)
                    pos = get_pos(board)
                # Sets current position value to numbers 1-9 in temp_board
                elif event.key == pygame.K_SPACE:
                    print("space")
                    solve(board, True)
                    solved = True
                    continue
                elif event.key == pygame.K_1:
                    set_value(temp_board, pos, 1)
                elif event.key == pygame.K_2:
                    set_value(temp_board, pos, 2)
                elif event.key == pygame.K_3:
                    set_value(temp_board, pos, 3)
                elif event.key == pygame.K_4:
                    set_value(temp_board, pos, 4)
                elif event.key == pygame.K_5:
                    set_value(temp_board, pos, 5)
                elif event.key == pygame.K_6:
                    set_value(temp_board, pos, 6)
                elif event.key == pygame.K_7:
                    set_value(temp_board, pos, 7)
                elif event.key == pygame.K_8:
                    set_value(temp_board, pos, 8)
                elif event.key == pygame.K_9:
                    set_value(temp_board, pos, 9)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                #  Check if board is empty, then set position to empty position.
                coord = convert_coord(pygame.mouse.get_pos())
                if board[coord[0]][coord[1]] == 0:
                    pos = coord
            if not solved:
                draw_board(temp_board, False)


