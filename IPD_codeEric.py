import random
import numpy as np
import math

def print_board(board):
    horizontal_line = "+---+---+---+"
    print(horizontal_line)
    print("| {} | {} | {} |".format(board[0], board[1], board[2]))
    print(horizontal_line)
    print("| {} | {} | {} |".format(board[3], board[4], board[5]))
    print(horizontal_line)
    print("| {} | {} | {} |".format(board[6], board[7], board[8]))
    print(horizontal_line)
    print()


def get_empty_cells(board):
    return [i for i in range(len(board)) if board[i] == " "]

def isWinner(board, player):
    for i in range(0, 9, 3):
        if board[i:i+3] == [player]*3:
            return True
    for i in range(3):
        if board[i::3] == [player]*3:
            return True
    if board[0] == player and board[4] == player and board[8] == player:
        return True
    if board[2] == player and board[4] == player and board[6] == player:
        return True
    return False

def minimax(board, depth, maximizing_player):
    if isWinner(board, "O"):
        return {"score": 10 - depth}
    elif isWinner(board, "X"):
        return {"score": depth - 10}
    elif not get_empty_cells(board):
        return {"score": 0}
    if maximizing_player:
        best_score = -math.inf
        for cell in get_empty_cells(board):
            board[cell] = "O"
            score = minimax(board, depth+1, False)["score"]
            board[cell] = " "
            if score > best_score:
                best_score = score
                best_cell = cell
        return {"score": best_score, "cell": best_cell}
    else:
        best_score = math.inf
        for cell in get_empty_cells(board):
            board[cell] = "X"
            score = minimax(board, depth+1, True)["score"]
            board[cell] = " "
            if score < best_score:
                best_score = score
                best_cell = cell
        return {"score": best_score, "cell": best_cell}

def NedMove(board):
    return minimax(board, 0, True)["cell"]

def playerMove(board):
    while True:
        cell = int(input("Enter a number between 0 and 8: "))
        if cell in get_empty_cells(board):
            return cell
        print("Invalid cell. Please try again.")

def tic_tac_toe():
    board = [" "]*9
    print_board(board)
    while True:
        cell = playerMove(board)
        board[cell] = "X"
        print_board(board)
        if isWinner(board, "X"):
            print("You win!")
            break
        if not get_empty_cells(board):
            print("Tie!")
            break
        cell = NedMove(board)
        board[cell] = "O"
        print_board(board)
        if isWinner(board, "O"):
            print("You lose!")
            break
        if not get_empty_cells(board):
            print("Tie!")
            break

tic_tac_toe()
