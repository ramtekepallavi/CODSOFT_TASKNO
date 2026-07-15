import math

board = [" " for _ in range(9)]

HUMAN = "X"
AI = "O"


def print_board():
    print("\n")
    print("-------------")
    print("|", board[0], "|", board[1], "|", board[2], "|")
    print("-------------")
    print("|", board[3], "|", board[4], "|", board[5], "|")
    print("-------------")
    print("|", board[6], "|", board[7], "|", board[8], "|")
    print("-------------")
    print()


def print_positions():
    print("\nBoard Positions")
    print("-------------")
    print("| 1 | 2 | 3 |")
    print("-------------")
    print("| 4 | 5 | 6 |")
    print("-------------")
    print("| 7 | 8 | 9 |")
    print("-------------")


def check_winner(player):
    wins = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    for line in wins:
        if board[line[0]] == board[line[1]] == board[line[2]] == player:
            return True
    return False


def board_full():
    return " " not in board


def minimax(is_ai):
    if check_winner(AI):
        return 1

    if check_winner(HUMAN):
        return -1

    if board_full():
        return 0

    if is_ai:
        best = -math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = AI
                score = minimax(False)
                board[i] = " "
                best = max(best, score)

        return best

    else:
        best = math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = HUMAN
                score = minimax(True)
                board[i] = " "
                best = min(best, score)

        return best


def ai_move():
    best_score = -math.inf
    move = -1

    for i in range(9):
        if board[i] == " ":
            board[i] = AI
            score = minimax(False)
            board[i] = " "

            if score > best_score:
                best_score = score
                move = i

    board[move] = AI


def human_move():
    while True:
        try:
            pos = int(input("Enter position (1-9): "))

            if pos < 1 or pos > 9:
                print("Choose between 1 and 9.")
                continue

            if board[pos-1] != " ":
                print("Position already occupied.")
                continue

            board[pos-1] = HUMAN
            break

        except ValueError:
            print("Enter a valid number.")


def game():
    print("="*40)
    print(" TIC TAC TOE AI ")
    print("="*40)

    print_positions()

    while True:

        print_board()

        human_move()

        if check_winner(HUMAN):
            print_board()
            print("🎉 Congratulations! You Win.")
            break

        if board_full():
            print_board()
            print("Game Draw!")
            break

        print("AI is thinking...")
        ai_move()

        if check_winner(AI):
            print_board()
            print("AI Wins!")
            break

        if board_full():
            print_board()
            print("Game Draw!")
            break


game()