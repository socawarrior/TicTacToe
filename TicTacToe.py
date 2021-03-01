import os

def clear_output():
    os.system('cls')


def display_game(gamelist):
    # print out board
    print('')
    print('')
    print(gamelist[0][0] + ' | ' + gamelist[0][1]  + ' | ' + gamelist[0][2])
    print('---------')
    print(gamelist[1][0] + ' | ' + gamelist[1][1]  + ' | ' + gamelist[1][2])
    print('---------')
    print(gamelist[2][0] + ' | ' + gamelist[2][1]  + ' | ' + gamelist[2][2])


def player1_move():
    # get input from a user to choose location
    board_options = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    player1choice = 'wrong'
    while player1choice not in board_options:
        player1choice = input("Player 1, please choose your position (1-9):")
        clear_output()
        display_game(gamelist)

    # dictionary containing the board # (1-9) and its coordinates
    board_library = {1: [2, 0], 2: [2, 1], 3: [2, 2], 4: [1, 0], 5: [1, 1], 6: [1, 2], 7: [0, 0], 8: [0, 1], 9: [0, 2]}

    # assigning coordinates based on user input
    y = board_library[int(player1choice)][0]
    x = board_library[int(player1choice)][1]

    # assinging the user's location a mark
    if gamelist[y][x] == ' ':
        gamelist[y][x] = 'X'
        clear_output()
        display_game(gamelist)
        return True
    else:
        clear_output()
        display_game(gamelist)
        print("sorry that's taken, try again!")
        return False



def player2_move():
    # get input from a user to choose location
    board_options = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    player2choice = 'wrong'
    while player2choice not in board_options:
        player2choice = input("Player 2, please choose your position (1-9):")
        clear_output()
        display_game(gamelist)

    # dictionary containing the board # (1-9) and its coordinates
    board_library = {1: [2, 0], 2: [2, 1], 3: [2, 2], 4: [1, 0], 5: [1, 1], 6: [1, 2], 7: [0, 0], 8: [0, 1], 9: [0, 2]}

    # assigning coordinates based on user input
    y = board_library[int(player2choice)][0]
    x = board_library[int(player2choice)][1]

    # trurning true and assinging the user's location a mark if the space is empty,
    # otherwise return false and display a message
    if gamelist[y][x] == ' ':
        gamelist[y][x] = 'O'
        clear_output()
        display_game(gamelist)
        return True
    else:
        clear_output()
        display_game(gamelist)
        print("sorry that's taken, try again!")
        return False



def play_game():
    # set won equal to false and create a list of 9 turns
    won = False
    turns = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # for loop through the turns, with a condition that if won is false, then check if the turn is even or odd
    # there is another condition depending on if the move function returns true or false, if false play again
    # a player will move accordingly, otherwise break out of the loop if someone wins
    for turn in turns:
        while won == False:
            if turn % 2 == 0:
                valid = player2_move()
                if valid == True:
                    won = game_check()
                    break
                else:
                    player2_move()
                    continue
            else:
                valid = player1_move()
                if valid == True:
                    won = game_check()
                    break
                else:
                    player1_move()
                    continue
        else:
            break


def game_check():
    # this function checks if across, vertically, and diagonal for 3 consecutive values (X or O). It is a while loop
    # and prints "you win!" if this condition is true, returns true for the playgame() function, and breaks out of the loop.

    acceptable_values = ['X', 'O']
    win = False
    # across check
    while win == False:
        if gamelist[0][0] == gamelist[0][1] == gamelist[0][2] and gamelist[0][0] in acceptable_values:
            win = True
            print('You win!')
            return True
        elif gamelist[1][0] == gamelist[1][1] == gamelist[1][2] and gamelist[1][0] in acceptable_values:
            win = True
            print('You win!')
            return True
        elif gamelist[2][0] == gamelist[2][1] == gamelist[2][2] and gamelist[2][0] in acceptable_values:
            win = True
            print('You win!')
            return True
        # vertical check
        elif gamelist[0][0] == gamelist[1][0] == gamelist[2][0] and gamelist[0][0] in acceptable_values:
            win = True
            print('You win!')
            return True
        elif gamelist[0][1] == gamelist[1][1] == gamelist[2][1] and gamelist[0][1] in acceptable_values:
            win = True
            print('You win!')
            return True
        elif gamelist[0][2] == gamelist[1][2] == gamelist[2][2] and gamelist[0][2] in acceptable_values:
            win = True
            print('You win!')
            return True
        # diagnal check
        elif gamelist[0][0] == gamelist[1][1] == gamelist[2][2] and gamelist[0][0] in acceptable_values:
            win = True
            print('You win!')
            return True
        elif gamelist[0][2] == gamelist[1][1] == gamelist[2][0] and gamelist[0][2] in acceptable_values:
            win = True
            print('You win!')
            return True
        else:
            return False


def continuegame():
    letsgo = 'wrong'
    values =['Y','y','N','n']
    while letsgo not in values:
        letsgo = input('would you like to keep playing? (Y/N)')
        clear_output()
        display_game(gamelist)

    if letsgo.lower() == 'y':
        return True
    else:
        return False




playagain = True

while playagain == True:
    # display board
    gamelist = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    display_game(gamelist)

    # play game
    play_game()

    # ask if use wants to continue and clear screen
    playagain = continuegame()
    clear_output()