
X = "X"
O = "O"
EMPTY = " "
TIE = "Ничья"
NUM_SQUARES = 9


def display_instruction():
    """Выводит инструкцию для игрока"""

    print("""Привет! Это игра "Крестики-нолики".
Чтобы сделать ход, введи номер клетки,
куда хочешь поставить свой символ:
    ..........

    0 | 1 | 2
    3 | 4 | 5
    6 | 7 | 8

    """)


def ask_yes_no(question):
    response = ""
    while response not in ("yes", "no"):
        response = input(question).lower()
    return response


def ask_number(question, low, high):
    """Запрос числа в заданном диапазоне"""
    response = ""
    while response not in range(low, high):
        response = int(input(question))
    return response


def pieces():
    """Выбор, кто ходит первый"""
    go_first = ask_yes_no("Хочешь ли ты походить первый, напиши yes или no")
    if go_first == "yes":
        print("Ты выбрал ходить первый, тебе крестики")
        human = X
        computer = O
    else:
        print("Что ж, я похожу первый")
        human = O
        computer = X
    return human, computer


def new_board():
    """Создает новую игровую доску"""
    board = []
    for quare in range(NUM_SQUARES):
        board.append(EMPTY)
    return board


def display_board(board):
    """Отображает игровую доску на экране"""
    print("\n\t", board[0], "|", board[1], "|", board[2])
    print("\t", board[3], "|", board[4], "|", board[5])
    print("\t", board[6], "|", board[7], "|", board[8], "\n")


def legal_moves(board):
    """Возвращает список доступных ходов"""
    moves = []
    for index in range(NUM_SQUARES):
        if board[index] == EMPTY:
            moves.append(index)
    return moves


def winner(board):
    """Определяет победителя в игре."""
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


def human_move(board, human):
    """Получает ход человека"""
    legal = legal_moves(board)
    move = ""
    while move not in legal:
        move = ask_number("Выбери ход (0-8)", 0, NUM_SQUARES)
        if move not in legal:
            print("Поле занято, выбери другое")
    return move


def computer_move(board, computer, human):
    board = board[:]
    BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)

    for move in legal_moves(board):
        board[move] = computer
        if winner(board) == computer:
            print(move)
            return move
        board[move] = EMPTY

    for move in legal_moves(board):
        board[move] = human
        if winner(board) == human:
            print(move)
            return move
        board[move] = EMPTY

    for move in BEST_MOVES:
        if move in legal_moves(board):
            print(move)
            return move


def next_turn(turn):
    if turn == X:
        return O
    else:
        return X


def congrat_winner(the_winner, computer, human):
    if the_winner == TIE:
        print("Ничья")
    elif the_winner == computer:
        print("Победил компутер")
    elif the_winner == human:
        print("Человек победил")


def main():
    answer = "yes"
    display_instruction()
    computer,human = pieces()
    turn = O
    board = new_board()
    display_board(board)
    while not winner(board):
        if turn == human:
            hod = human_move(board, human)
            board[hod] = human
        else:
            hod = computer_move(board, computer, human)
            board[hod] = computer
        display_board(board)
        turn = next_turn(turn)
    pobeditel = winner(board)
    congrat_winner(pobeditel, computer, human)
    answer = input('Хочешь отыграться?')
    while answer == "yes":
        main()


# запуск программы
main()
input("Нажмите enter чтобы выйти")