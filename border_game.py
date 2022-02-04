BLACK = 'B'
WHITE = 'W'
EMPTY = 'E'

def has_move(board, line, column):
    """ Given a board with Black, White and Empty slots, this functions must
    calculate if starting from line and column defined as parameters the are
    empty slots that can be occupied.

    Imagine each player start with a position occupied. So the first can occupy
    any adjacent Empty slot. After that the second player can do the same and so
    on until there is no more Empty slot adjacent to any occupied one.

    :param board: Matrix m x n
    :param line: The line of start slot
    :param column: The column of start slot
    :return: True if there is any Empty slot adjacent to the are occupied by one player
    """

board_white_unfinished = [
    [EMPTY, WHITE, BLACK, EMPTY],
    [EMPTY, WHITE, BLACK, EMPTY],
    [EMPTY, WHITE, BLACK, EMPTY],
    [EMPTY, WHITE, BLACK, EMPTY],
]
board_white_finished = [
    [WHITE, WHITE, BLACK, BLACK],
    [WHITE, WHITE, BLACK, BLACK],
    [WHITE, WHITE, BLACK, BLACK],
    [WHITE, WHITE, BLACK, EMPTY]
]

print(has_move(board_white_unfinished, 1,1)) # expected True
print(has_move(board_white_finished, 1,1)) # expected False