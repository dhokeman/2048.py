print("Welcome to 2048-The Game")
print("General Instructions")
print("1.For Moves use w,a,s and d for up,right,down and left respectively(Press enter after each move)\n2.Default board size will be 5*5 while win shall be on 2048 score\n3.Enter 1 for default values or you may enter values as per your convinience")
print("4.restart game-r")
size=int(input('Enter game board size(1 for default ):'))
if size==1:
    n=5
if size > 1:
    n=size
if size<=0:
    n=5
    print('size cannot be negative or zero so default value of 5*5 is taken')

score=int(input('Enter winning score(1 for default )(enter value which is even multiple of 2):'))
if score==1:
    win=2048
else:
    win=score
#game board
global board
board=[list(range(1+n*i,1+n*(i+1)))
           for i in range(n)]
for i in range(n):
    for j in range(n):
        board[i][j]=0

#function to spawn random 2
def ran2():
    global temp
    global board
    d=int(100)
    for i27 in range(n):
        for j27 in range(n):
            if board[i27][j27] ==0:
                d=0
                break

    if d==100:
        print("You Loose")
        print("Do you want to undo last move?")
        y=input('press yes or no:')
        we=int(0)
        if y=="yes":
            board=temp
            return game2048()
        if y=="no":

            we=100
        if we==100:
            print('Thank you for playing.\nWe wish to see you soon')
        else:
            return


    import random
    p = int(random.randint(0, n - 1))
    q = int(random.randint(0, n - 1))
    if board[p][q] == 0:
        board[p][q] = 2

    else:
        ran2()

#up move
def up():
    def adjacent_up():
        for i100 in range(n):
            for i1 in range(n):
                for j1 in range(n - 1):
                    if board[j1][i1] == 0:
                        board[j1][i1] = board[j1 + 1][i1]
                        board[j1 + 1][i1] = 0


    adjacent_up()
    for i in range(n):
        for j in range(n - 1):
            if board[j][i] == board[j + 1][i]:
                board[j][i] = 2 * board[j + 1][i]
                board[j + 1][i] = 0
    adjacent_up()
#for down move
def down():
    def adjacent_down():
        for i81 in range(n):
            for i in range(n):

                for j in range(n - 1, 0, -1):
                    if board[j][i] == 0:
                        board[j][i] = board[j - 1][i]
                        board[j - 1][i] = 0
    adjacent_down()
    for i in range(n):
        for j in range(n - 1, 0, -1):
            if board[j][i]==board[j-1][i]:
                board[j][i]=2*board[j-1][i]
                board[j-1][i]=0
    adjacent_down()

#for left move
def left():
    def adjacent_left():
        for i10 in range(n):
            for i3 in range(n):
                for j3 in range(n - 1):
                    if board[i3][j3] == 0:
                        board[i3][j3] = board[i3][j3+1]
                        board[i3][j3+1] = 0


    adjacent_left()
    for i in range(n):
        for j in range(n - 1):
            if board[i][j] == board[i][j+1]:
                board[i][j] = 2 * board[i][j+1]
                board[i][j+1] = 0
    adjacent_left()
#right move
def right():
    def adjacent_right():
        for p69 in range(n):
            for i39 in range(n):
                for j39 in range(n - 1, 0, -1):
                    if board[i39][j39] == 0:
                        board[i39][j39] = board[i39][j39 - 1]
                        board[i39][j39 - 1] = 0

    adjacent_right()
    for i68 in range(n):
        for j68 in range(n - 1,0,-1):
            if board[i68][j68] == board[i68][j68-1]:
                board[i68][j68] = 2 * board[i68][j68-1]
                board[i68][j68-1] = 0
    adjacent_right()

ran2()
import copy
temp = copy.copy(board)
def game2048():
    global board
    global temp
    import copy
    temp = copy.copy(board)



    for r in board:
            for c in r:
                print(c, end="   ")
            print('\n ')


    move=input()
    if move =="w":
        up()
    elif move=="a":
        left()
    elif move=="s":
        down()
    elif move=="d":
        right()
    elif move=="r":
        board = [list(range(1 + n * i, 1 + n * (i + 1)))
                 for i in range(n)]
        for i in range(n):
            for j in range(n):
                board[i][j] = 0
        ran2()

    else:
        print("OoOpsS!!...something went wrong\nTry Again\nGeneral Instructions\n1.w-up\n2.a-left\n3.s-down\n4.d-right\n5.r-restart game")
        game2048()
    if move!="r":
        for i in range(n):
            op=int(69)
            for j in range(n):
                if temp[i][j] !=(board[i][j]):
                    op=0

        if op==0:
            print('oops!! not a legal move.\nTry again')
            game2048()


        else:
            ran2()


    m=int(0)
    for i23 in range(n):
        for j23 in range(n):
            if board[i23][j23] == win:
                m=100

    if m==100:
        print("Congratulations!You win")
    else:
        return game2048()



game2048()