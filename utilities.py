def isEmptyCell(board, col):
    if board[0][col] == 0:
        return True
    return False


def getBestPositionRefined(board, depth):
    best_score = float("-inf")
    global bestPos
    alpha = float("-inf")
    beta = float("inf")
    for col in getPossibleMoves(board):
        row = getUpcomingEmptyRow(board, col)
        board_copy = board.copy()
        board_copy[row][col] = 2
        score = refinedMinimax(board_copy, depth - 1, alpha, beta, False)
        if score > best_score:
            best_score = score
            bestPos = col
        alpha = max(alpha, score)
    return bestPos


def getBestPositionNormal(board, depth):
    best_score = float("-inf")
    global bestPos
    for col in getPossibleMoves(board):
        row = getUpcomingEmptyRow(board, col)
        board_copy = board.copy()
        board_copy[row][col] = 2
        score = normalMinimax(board_copy, depth - 1, False)
        if score > best_score:
            best_score = score
            bestPos = col
    return bestPos


def getUpcomingEmptyRow(board, c):
    for row in reversed(range(6)):
        if board[row][c] == 0:
            return row
    return -1


