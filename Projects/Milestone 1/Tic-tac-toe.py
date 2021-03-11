def setup():
    print('This game is the popular X and O game. 2 players will choose their marker uppercase X or O')
    print('The board of the game is as shown below. Your marker X or O will be placed in the same position')
    print('of the numbers you input as it is on the board. Kindly take note of this numbers and their position')
    print ('You know the rules of X and O, so lets get to it. Have fun!')
    print (' ||     ||     ||     ||')
    print (' || (1) || (2) || (3) ||')
    print (' ||_____||_____||_____||')
    print (' ||     ||     ||     ||')
    print (' || (4) || (5) || (6) ||')
    print (' ||_____||_____||_____||')
    print (' ||     ||     ||     ||')
    print (' || (7) || (8) || (9) ||')
    print (' ||     ||     ||     ||')
    

    global board, board2, p, player1, player2, pp, mark
    board = [1,2,3,4,5,6,7,8,9]
    board2 = [1,2,3,4,5,6,7,8,9]
    p=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    pp=['i','j','k','l','m','n','o','p','q']
    mark=True
    while mark:
        player1 = input('Choose your marker Player 1, uppercase X or O ')
        if player1 == 'X':
            player2 = 'O'
            print ('Player1 your marker is X')
            print ('Player2 your marker is O')
            mark= False
            continue
        elif player1 == 'O':
            player2 = 'X'
            print ('Player1 your marker is O')
            print ('Player2 your marker is X')
            mark= False
            continue            
        else:
            print ('Player 1 enter uppercase X or O for your marker, thanks.')
            
    gameplay()

pass

from IPython.display import clear_output
def boardprnt():
    clear_output()
    print (' ||     ||     ||     ||')
    print (f' ||  {p[0]}  ||  {p[1]}  ||  {p[2]}  ||')
    print (' ||_____||_____||_____||')
    print (' ||     ||     ||     ||')
    print (f' ||  {p[3]}  ||  {p[4]}  ||  {p[5]}  ||')
    print (' ||_____||_____||_____||')
    print (' ||     ||     ||     ||')
    print (f' ||  {p[6]}  ||  {p[7]}  ||  {p[8]}  ||')
    print (' ||     ||     ||     ||')
    

pass

def endgame():
    replay = input ('Do you want to play again? Enter upper case Y or N ')
    if replay == 'Y':
        startgame()
    else:
        print ('Thanks for playing! Tschuss')
    
pass


def gameplay():
    gturn1 = True
    gturn2 = False
    replay= ''
    for item in range(0,9):
        
        while gturn1:
            gamer1 = int(input("Player 1 Enter the number corresponding to where you want to place your marker according to the game's instruction"))
            if gamer1 in board:
                indexer1=board2.index(gamer1)
                p[indexer1]= player1
                pp[indexer1]= player1
                board.remove(gamer1)
                boardprnt()
                gturn2= True
                gturn1= False
                decider ()
                if p[9] == 'endgame':
                    gturn2= False
                if item == 4:
                    gturn2= False
                    print ('There is a tie!')
                    replay = input ('Do you want to play again? Enter upper case Y or N ')
                    if replay == 'Y':
                        startgame()
                    else:
                        endgame()
                continue
            else:
                print ('Player 1 Please enter a number between 1-9 that has not already been used')        
 
        while gturn2:
            gamer2 = int(input("Player 2 Enter the number corresponding to where you want to place your marker according to the game's instruction"))
            if gamer2 in board:
                indexer2=board2.index(gamer2)
                p[indexer2]= player2
                pp[indexer2]= player2
                board.remove(gamer2)
                boardprnt()                 
                gturn2= False      
                gturn1= True
                decider ()
                if p[9] == 'endgame':
                    gturn1= False
                if item == 3:
                    gturn1= False
                    print ('There is a tie!')
                    replay = input ('Do you want to play again? Enter upper case Y or N ')
                    if replay == 'Y':
                        startgame()
                    else:
                        print ('Thanks for playing! Tschuss')
                continue
            else:
                print ('Player 1 Please enter a number between 1-9 that has not already been used')      
    if p[9] == 'endgame':
        endgame() 


pass


def decider ():
    deal = True
    while deal:
        if pp[0]==pp[1]==pp[2]:
            deal= False
            p[9] = 'endgame'
            if player1 == pp[0]==pp[1]==pp[2]:
                print (f'Player 1 has won!, {p[0]} has won!') 
            elif player2 == pp[0]==pp[1]==pp[2]:
                print (f'Player 2 has won!, {p[0]} has won!')
        elif pp[0]==pp[3]==pp[6]:
            deal= False
            p[9] = 'endgame'
            if player1 == pp[0]==pp[3]==pp[6]:
                print (f'Player 1 has won!, {p[0]} has won!')
                
            elif player2 == pp[0]==pp[3]==pp[6]:
                print (f'Player 2 has won!, {p[0]} has won!')
                
        elif pp[0]==pp[4]==pp[8]:
            deal= False
            p[9] = 'endgame'
            if player1 == pp[0]==pp[4]==pp[8]:
                print (f'Player 1 has won!, {p[0]} has won!')
               
            elif player2 == pp[0]==pp[4]==pp[8]:
                print (f'Player 2 has won!, {p[0]} has won!')
                
        elif pp[1]==pp[4]==pp[7]:
            deal= False
            p[9] = 'endgame'
            if player1 == pp[1]==pp[4]==pp[7]:
                print (f'Player 1 has won!, {p[1]} has won!')
               
            elif player2 == pp[1]==pp[4]==pp[7]:
                print (f'Player 2 has won!, {p[1]} has won!')
             
        elif pp[2]==pp[5]==pp[8]:
            deal= False
            p[9] = 'endgame'
            if player1 == pp[2]==pp[5]==pp[8]:
                print (f'Player 1 has won!, {p[2]} has won!')
               
            elif player2 == pp[2]==pp[5]==pp[8]:
                print (f'Player 2 has won!, {p[2]} has won!')
               
        elif pp[2]==pp[4]==pp[6]:
            deal= False
            p[9] = 'endgame'
            if player1 == pp[2]==pp[4]==pp[6]:
                print (f'Player 1 has won!, {p[2]} has won!')
              
            elif player2 == pp[2]==pp[4]==pp[6]:
                print (f'Player 2 has won!, {p[2]} has won!')
              
        elif pp[3]==pp[4]==pp[5]:
            deal= False
            p[9] = 'endgame'
            if player1 == pp[3]==pp[4]==pp[5]:
                print (f'Player 1 has won!, {p[3]} has won!')
            
            elif player2 ==pp[3]==pp[4]==pp[5]:
                print (f'Player 2 has won!, {p[3]} has won!')
             
        elif pp[6]==pp[7]==pp[8]:
            deal= False
            p[9] = 'endgame'
            if player1 == pp[6]==pp[7]==pp[8]:
                print (f'Player 1 has won!, {p[6]} has won!')
              
            elif player2 == pp[6]==pp[7]==pp[8]:
                print (f'Player 2 has won!, {p[6]} has won!')
              
        else:
            deal= False
            continue
    
    
pass


def newgame ():
    from IPython.display import clear_output
    clear_output()
    setup()
    
newgame()