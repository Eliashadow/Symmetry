'''
something
'''

def transpose(board: list[list]) -> list[list]:
    """
    Creates new matrix with NxM instead of MxN

    :param board: list[list], A list with lists which represent board 

    :return: list[list], A list with lists which represents board reflected by main diagonal

    >>> board = [['0', 'x', '', '0'], ['0', 'x', '', '0'], ['', '', '', '0'], ['0', 'x', 'x', '0']]
    >>> transpose(board)
    [['0', '0', '', '0'], ['x', 'x', '', 'x'], ['', '', '', 'x'], ['0', '0', '0', '0']]
    >>> transpose(board) != board
    True
    >>> board = None
    >>> transpose(board)
    """

    if not board or not board[0]:
        return None

    m, n = len(board), len(board[0])
    transformed_board = [[board[row][col] for row in range(m)] for col in range(n)]

    return transformed_board


def flip(board: list[list], h_axis: bool = False, v_axis: bool = False) -> list[list]:
    """
    Creates new matrix with reflection by horizontal or vertical axis

    :param board: list[list], A list with lists which represent board 
    :param h_axis: bool, by default False, A setting to make vertical flip
    :param v_axis: bool, by default False, A setting to make horizontal flip

    :return: list[list], A list with lists which represents board reflected by applied axis

    >>> board = None
    >>> flip(board)
    >>> board = [['0', 'x', '', '0'], ['0', 'x', '', '0'], ['', '', '', '0'], ['0', 'x', 'x', '0']]
    >>> flip(board)
    [['0', 'x', '', '0'], ['0', 'x', '', '0'], ['', '', '', '0'], ['0', 'x', 'x', '0']]
    >>> flip(board, True)
    [['0', 'x', 'x', '0'], ['', '', '', '0'], ['0', 'x', '', '0'], ['0', 'x', '', '0']]
    >>> flip(board, True) != board
    True
    >>> flip(board, v_axis = True)
    [['0', '', 'x', '0'], ['0', '', 'x', '0'], ['0', '', '', ''], ['0', 'x', 'x', '0']]
    >>> flip(board, True, True)
    [['0', 'x', 'x', '0'], ['0', '', '', ''], ['0', '', 'x', '0'], ['0', '', 'x', '0']]
    """

    if not board or not board[0]:
        return None

    transformed_board = board[::]

    m, n = len(board), len(board[0])
    if v_axis and h_axis:
        transformed_board = [[board[row][j-1] for j in range(n, 0, -1)] for row in range(m)]
        transformed_board = [transformed_board[i-1] for i in range(m, 0, -1)]
    elif h_axis:
        transformed_board = [board[i-1] for i in range(m, 0, -1)]
    elif v_axis:
        transformed_board = [[board[row][j-1] for j in range(n, 0, -1)] for row in range(m)]

    return transformed_board


def create_numbered_board(board: list[list]) -> list[list]:
    """
    Creates numbered board

    >>> board = [['0', 'x', '', '0'], ['0', 'x', '', '0'], ['', '', '', '0'], ['0', 'x', 'x', '0']]
    >>> create_numbered_board(board)
    [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]

    """

    m, n = len(board), len(board[0])
    numbered_board = []

    counter = 0
    for _ in range(m):
        row = []
        for _ in range(n):
            row.append(counter)
            counter += 1
        numbered_board.append(row)

    return numbered_board


def permutation(board: list[list]) -> list[tuple[list, str]] | None:
    '''
    rewrite this docstring
    Applies changes to the board in this order:
    1. 0
    2. 90
    3. 180
    4. 270
    5. Flip vertical
    6. Flip horizontal
    7. Main diagonal
    8. Sup diagonal
    >>> board = [['0', 'x', '', '0'], ['0', 'x', '', '0'], ['', '', '', '0'], ['0', 'x', 'x', '0']]
    >>> permutation(board)
    [([['0', 'x', '', '0'], ['0', 'x', '', '0'], ['', '', '', '0'], ['0', 'x', 'x', '0']], '0'), \
([['0', '', '0', '0'], ['x', '', 'x', 'x'], ['x', '', '', ''], ['0', '0', '0', '0']], '90'), \
([['0', 'x', 'x', '0'], ['0', '', '', ''], ['0', '', 'x', '0'], ['0', '', 'x', '0']], '180'), \
([['0', '0', '0', '0'], ['', '', '', 'x'], ['x', 'x', '', 'x'], ['0', '0', '', '0']], '270'), \
([['0', 'x', 'x', '0'], ['', '', '', '0'], ['0', 'x', '', '0'], ['0', 'x', '', '0']], 'v'), \
([['0', '', 'x', '0'], ['0', '', 'x', '0'], ['0', '', '', ''], ['0', 'x', 'x', '0']], 'h'), \
([['0', '0', '', '0'], ['x', 'x', '', 'x'], ['', '', '', 'x'], ['0', '0', '0', '0']], 'd1'), \
([['0', '0', '0', '0'], ['x', '', '', ''], ['x', '', 'x', 'x'], ['0', '', '0', '0']], 'd2')]
    '''

    if not board or not board[0]:
        return None

    permutations = [(board, '0'),
                    (flip(transpose(board), v_axis=True), '90'),
                    (flip(board, True, True), '180'),
                    (transpose(flip(board, v_axis=True)), '270'),
                    (flip(board, h_axis=True), 'v'),
                    (flip(board, v_axis=True), 'h'),
                    (transpose(board), 'd1'),
                    (transpose(flip(board, True, True)), 'd2')
            ]

    correct_permutations = []

    m, n = len(board), len(board[0])

    for perm, name in permutations:
        # Checking for non-squared boards
        if (len(perm) == m and len(perm[0]) == n):
            # Checking for duplicates
            if all(perm[0] != item[0] for item in correct_permutations):
                correct_permutations.append((perm, name))

    return correct_permutations


def is_invariant(board: list[list]) -> list[str] | None:
    '''
    Checks if applied permutations changed board
    >>> board = [['0', 'x', '', '0'], ['0', 'x', '', '0'], ['', '', '', '0'], ['0', 'x', 'x', '0']]
    >>> len(is_invariant(board)) in (1, 2, 4, 8)
    True
    >>> is_invariant(board)
    ['0']
    >>> board = [['x', '', 'x'], ['', '0', ''], ['x', '', 'x']]
    >>> len(is_invariant(board))
    8
    '''

    if not board or not board[0]:
        return None

    m, n = len(board), len(board[0])
    numbered_board = create_numbered_board(board)
    valid_symmetries = permutation(numbered_board)

    result = []
    for num_board, name in valid_symmetries:
        is_same = True
        for row in range(m):
            for col in range(n):
                pos_num = num_board[row][col]
                orig_row = pos_num // n
                orig_col = pos_num % n
                if board[row][col] != board[orig_row][orig_col]:
                    is_same = False
                    break
            if not is_same:
                break

        if is_same:
            result.append(name)

    if len(result) in (1, 2, 4, 8):
        return result

    return None


if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
