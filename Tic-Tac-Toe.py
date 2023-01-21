import random
import time
print("Tic, Tac, Toe")
player_name = input("What is your name? ")
player_wins = 0
computer_wins = 0

while True:
    board = [" " for x in range(9)]

    def print_board():
        row1 = "| {} | {} | {} |".format(board[0], board[1], board[2])
        row2 = "| {} | {} | {} |".format(board[3], board[4], board[5])
        row3 = "| {} | {} | {} |".format(board[6], board[7], board[8])

        print()
        print(row1)
        print(row2)
        print(row3)
        print()

    def player_move(icon):
        while True:
            print("Your turn, " + player_name + "!")
            try:
                choice = int(input("Enter your move (1-9): ").strip())
                if choice < 1 or choice > 9:
                    raise ValueError
                if board[choice - 1] == " ":
                    board[choice - 1] = icon
                    break
                else:
                    print()
                    print("That space is taken!")
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 9")

    def computer_move(icon):
        print("Computer's turn")
        while True:
            choice = random.randint(0,8)
            if board[choice] == " ":
                board[choice] = icon
                break

    def is_victory(icon):
        if (board[0] == icon and board[1] == icon and board[2] == icon) or \
            (board[3] == icon and board[4] == icon and board[5] == icon) or \
            (board[6] == icon and board[7] == icon and board[8] == icon) or \
            (board[0] == icon and board[3] == icon and board[6] == icon) or \
            (board[1] == icon and board[4] == icon and board[7] == icon) or \
            (board[2] == icon and board[5] == icon and board[8] == icon) or \
            (board[0] == icon and board[4] == icon and board[8] == icon) or \
            (board[2] == icon and board[4] == icon and board[6] == icon):
            return True
        else:
            return False


    def is_draw():
        if " " not in board:
            return True
        else:
            return False
    while True:
        print_board()
        player_move("X")
        print_board()
        if is_victory("X"):
            player_wins += 1
            print(f"{player_name} wins! Congratulations!")
            break
        elif is_draw():
            print("It's a draw!")
            break
        computer_move("O")
        if is_victory("O"):
            print_board()
            computer_wins +=1
            print("Computer wins! Better luck next time!")
            break
        elif is_draw():
            print("It's a draw!")
            break
    print(f"{player_name} wins: {player_wins}, Computer wins: {computer_wins}")
    play_again = ""
    while True:
        play_again = input("Do you want to play again? (y/n)")
        if play_again.upper() in ["Y", "YES"]:
            board = [" " for x in range(9)]  # Reset the board
            break
        elif play_again.upper() in ["N", "NO"]:
            print("Thanks for playing!")
            time.sleep(2)
            exit()
        else:
            print("Invalid input. Please enter y or n")