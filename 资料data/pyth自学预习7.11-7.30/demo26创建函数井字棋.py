# Tic-Tac-Toe  井字棋
# 和人类对手下井字棋
   
# global constants 全局常量
X = "X"
O = "O"
EMPTY = " "
TIE = "TIE"
NUM_SQUARES = 9

#1.定义 显示游戏说明函数
def display_instruct():
    """Display game instructions."""  
    print(
    """
    Welcome to the greatest intellectual challenge of all time: Tic-Tac-Toe.  
    This will be a showdown between your human brain and my silicon processor.  

    You will make your move known by entering a number, 0 - 8.  The number 
    will correspond to the board position as illustrated:
    
                    0 | 1 | 2
                    ---------
                    3 | 4 | 5
                    ---------
                    6 | 7 | 8

    Prepare yourself, human.  The ultimate battle is about to begin. \n
    """
    )

#2.定义 询问是或者否的函数
def ask_yes_no(question):
    """Ask a yes or no question."""
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response

#3.定义 请求用户给出指定范围内数字的函数
def ask_number(question, low, high):
    """Ask for a number within a range."""
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response

#4.定义 询问玩家是否希望先行棋，根据传统，X先走
def pieces():
    """Determine if player or computer goes first."""
    go_first = ask_yes_no("你希望先走第一步棋吗？ (y/n): ")
    if go_first == "y":
        print("\n你走第一步棋。")
        human = X
        computer = O
    else:
        print("\n你很勇敢，我先来。.")
        computer = X
        human = O
    return computer, human

#5.定义 创建棋盘列表函数，一个长度为9的列表，各元素被设置为空格
def new_board():
    """Create new game board."""
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board

#6.定义 棋盘显示函数
def display_board(board):
    """Display game board on screen."""
    print("\n\t", board[0], "|", board[1], "|", board[2])
    print("\t", "---------")
    print("\t", board[3], "|", board[4], "|", board[5])
    print("\t", "---------")
    print("\t", board[6], "|", board[7], "|", board[8], "\n")

#7.定义 函数接收一个棋盘，并返回一组合法的行棋步骤
def legal_moves(board):
    """Create list of legal moves."""
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves

#8.定义 函数接受一个棋盘，然后判断输赢情况
def winner(board):
    """Determine the game winner."""
    WAYS_TO_WIN = ((0, 1, 2),
                   (3, 4, 5),
                   (6, 7, 8),
                   (0, 3, 6),
                   (1, 4, 7),
                   (2, 5, 8),
                   (0, 4, 8),
                   (2, 4, 6))
    
    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner

    if EMPTY not in board:
        return TIE

    return None

#9.定义 函数接收一个棋盘和玩家的棋子，它会返回玩家想要放子的方格编号。
def human_move(board, human):
    """Get human move."""  
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number("你要下在哪里？ (0 - 8):", 0, NUM_SQUARES)
        if move not in legal:
            print("\n愚蠢的人类，这个方格已经有棋子了，重新下棋。\n")
    print("额...")
    return move

#10.定义 函数接收一个棋盘以及机器人和玩家的棋子，返回机器人的行棋步骤。
def computer_move(board, computer, human):
    """Make computer move."""
    # 由于该函数会对列表造成修改，所以需要创造一个副本。
    board = board[:]
    # 优劣顺序排列的行棋位置
    BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)

    print("I shall take square number", end=" ")
    
    # 如果机器人能赢，就走那个位置
    for move in legal_moves(board):
        board[move] = computer
        if winner(board) == computer:
            print(move)
            return move
        # 结束对当前行棋方案的测试，并取消
        board[move] = EMPTY
    
    # 如果人类能赢，就堵住那个位置
    for move in legal_moves(board):
        board[move] = human
        if winner(board) == human:
            print(move)
            return move
        # 结束对当前行棋方案的测试，并取消
        board[move] = EMPTY

    # 由于本轮谁也赢不了，所以挑选最佳空位来走
    for move in BEST_MOVES:
        if move in legal_moves(board):
            print(move)
            return move

#11. 定义 函数接收当前行棋方，返回下一个行棋方
def next_turn(turn):
    """Switch turns."""
    if turn == X:
        return O
    else:
        return X

#12.定义 函数接收游戏的赢家，以及机器人和玩家的棋子  
def congrat_winner(the_winner, computer, human):
    """Congratulate the winner."""
    if the_winner != TIE:
        print(the_winner, "won!\n")
    else:
        print("It's a tie!\n")

    if the_winner == computer:
        print("正如我预测的那样，我又一次取得了胜利！ \n" \
              "计算机在所有方面都优于人类！")

    elif the_winner == human:
        print("不，不，！我怎么会输，卑鄙的人类！ \n" \
              "我发誓，这是最后一次！")

    elif the_winner == TIE:
        print("竟然是平局，你太幸运了！ \n" \
              "庆祝吧，人类，这是你所能取得的最好的成绩！")

#13. 定义 函数主体程序，习惯用法，函数封装
def main():
    display_instruct()
    computer, human = pieces()
    turn = X
    board = new_board()
    display_board(board)

    while not winner(board):
        if turn == human:
            move = human_move(board, human)
            board[move] = human
        else:
            move = computer_move(board, computer, human)
            board[move] = computer
        display_board(board)
        turn = next_turn(turn)

    the_winner = winner(board)
    congrat_winner(the_winner, computer, human)


# start the program启动程序
main()
input("\n\nPress the enter key to quit.")
