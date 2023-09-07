# Problem
# Tic Tac Toe

'''
Define Board
Print Board
Play game - Set players and start playing until winner or all position filled in
winner function
Offer to replay
'''

def defineBoard():
    board = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' }
    return board

# print Board
def boardPrint(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

# Game Function
def playTicTacToe(board):

    while True:
        p1 = input(("Player 1 - Choose X or O \n")).upper()
        if p1 == "X": 
            p2 = "O"
            break
        elif p1 == "O": 
            p2 = "X"
            break
        else: print("Enter Either X or O")
    
    print("Player 1 will play {0} and Player 2 will play {1}".format(p1,p2))         
    turn = p1
    cnt = 0
    
    while True:
        ch = input(" {0} - Enter Position to Play \n".format(turn))
        if int(ch) in range(1,9): 
            if board[ch] is " ":
                board[ch] = turn
                boardPrint(board)
                cnt += 1
                if cnt >= 5: winner(board, turn)
            else:
                print("Position already filled in..Enter again")
                continue

            if turn == p1: 
                turn = p2
            else: 
                turn = p1

            if cnt >= 9: 
                x = input("Its a tie..Do you want to play again? - y/n ?").upper()
                if x == "Y": startPlay()
                print("Thanks for Playing..bye")
                break
        else: 
            print("Incorrect Input {0}, Enter position 1-9 if not filled".format(ch))

# Decide winner
def winner(board, turn):
    winner = False
    if board['1'] == board['2'] == board['3'] != " ": 
        winner = True
    if board['4'] == board['5'] == board['6'] != " ": 
        winner = True
    if board['7'] == board['8'] == board['9'] != " ": 
        winner = True
    if board['1'] == board['4'] == board['7'] != " ": 
        winner = True
    if board['2'] == board['5'] == board['8'] != " ": 
        winner = True
    if board['3'] == board['6'] == board['9'] != " ": 
        winner = True
    if board['7'] == board['5'] == board['3'] != " ": 
        winner = True
    if board['1'] == board['5'] == board['9'] != " ": 
        winner = True

    if winner is True:
        print("We have a Winner -", turn)
        x = input("\n Do you want to play again? - y/n ?").upper()
        if x == "Y": 
            startPlay()
        else:
            print("Thanks for Playing..bye")
            exit()

def startPlay():
    board = defineBoard()
    boardPrint(board)
    playTicTacToe(board)

''' Driver Code '''
startPlay()