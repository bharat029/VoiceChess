import chess
import os 
from playsound import playsound

def loc_to_square(loc):
    FILE_NAMES = ["a", "b", "c", "d", "e", "f", "g", "h"]
    RANK_NAMES = ["1", "2", "3", "4", "5", "6", "7", "8"]
    return RANK_NAMES.index(loc[1]) * 8 + FILE_NAMES.index(loc[0])

def name_to_idx(piece_name):
    piece_type = ['pawn', 'knight', 'bishop', 'rook', 'queen', 'king']
    return piece_type.index(piece_name) + 1

def what(piece):
    if piece is None:
        return 'No piece on this tile'
    piece = str(piece)
    if piece == 'P':
        return 'White Pawn'
    elif piece == 'p':
        return 'Black Pawn'
    elif piece == 'R':
        return 'White Rook'
    elif piece == 'r':
        return 'Black Rook'
    elif piece == 'B':
        return 'White Bishop'
    elif piece == 'b':
        return 'Black Bishop'
    elif piece == 'N':
        return 'White Knight'
    elif piece == 'n':
        return 'Black Knight'
    elif piece == 'K':
        return 'White King'
    elif piece == 'k':
        return 'Black King'
    elif piece == 'Q':
        return 'White Queen'
    elif piece == 'q':
        return 'Black Queen'
    else:
        return piece
    
board = chess.Board()
turn = True

playsound('Audio\ltc.mp3')
choice = input('Would you like to continue the game from last time? (y/n)').lower()

if choice == 'y':
    with open('save_game.txt') as f:
        board.set_board_fen(f.read())

while not board.is_game_over():
    print(board.unicode())
    playsound('Audio\\' + 'nextcmd.mp3')
    print('Enter the command to move:')
    
    if turn:
        playsound('Audio\\wt.mp3')
        print('White\'s Turn:')
    else:
        playsound('Audio\\' + 'bt.mp3')
        print('Black\'s Turn:')
        
    command = input().lower()
    try:
        if command.startswith('where'):
            _, piece, colour = command.split()
            for i in board.pieces(name_to_idx(piece), colour == 'white'):
                playsound('Audio\\' + chess.square_name(i) + '.mp3')
                print(chess.square_name(i))
            input()
        elif command.startswith('what'):
            _, loc = command.split()
            playsound('Audio\\' + what(board.piece_at(loc_to_square(loc))) + '.mp3')
            print(what(board.piece_at(loc_to_square(loc))))
            input()
        elif command == 'exit':
            with open('save_game.txt', 'w') as f:
                f.write(board.board_fen())
                break
        else:
            board.push_uci(command)
            turn = not turn 
    except Exception as e:
        playsound('Audio\illegalmove.mp3')
        print('Illegal move')
        input()
    os.system('cls')
board.board_fen()
input()