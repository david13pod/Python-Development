from IPython.display import clear_output
clear_output()

class Gamerules():
    def carddeck (self):
        from random import shuffle
        #define a deck of card
        deck1=[2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace',2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace',2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace',2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
        deck2=[2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace',2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace',2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace',2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
        deck3=[2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace',2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace',2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace',2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
        self.deck4=deck1+deck2+deck3
        shuffle(self.deck4)

    def instructions (self):
        print(f'{self.name} welcome to Blackjack game \nThis is a card game, you will be paying against the '
              'dealer. \nThese are the rules of the game: \n\n1) You are given 2 random cards by the dealer and the dealer has 2 cards too\n'
              'The decisions you can make after receiving your cards: \nHit - collect more cards from the dealer \nStand' 
             ' - refuse to collect more cards from the dealer \nSplit - only possible if you have cards of same values'
             ' only after the dealer has given you your 2 cards, your bet is doubled and you receive another'
             ' card \nDouble - your bet is doubled and you are given another card by the dealer on each split \nSurrender -'
             ' the game ends immediately with you only getting half your bet back \n\n2) You win if you have Blackjack'
             '(if the addition of your cards is 21) or if the total value of your card is greater than the dealers'
             '\n\n3) You loose if the dealers card is greater \n\n4) You draw if you have same value with the dealer, however'
             ' if the number of cards are not the same, the person with the lowest number of cards wins\n\n')

    def winn (self):
        self.winnings= self.pbet * 1.5
        if self.splita != 'checkcheck':
            self.funddep += self.winnings
            print(f'You won your bet, balance is {self.funddep}')
        elif self.splita == 'checkcheck':
            self.funddep += self.winnings *0.5
            print(f'You won your bet, balance is {self.funddep}')
    def half (self):
        self.surrend = self.pbet * 0.5
        self.funddep += self.surrend
        print(f'You have lost half of your bet, balance is {self.funddep}')
    def dcredit (self):
        if self.splita != 'checkcheck':
            self.funddep += self.pbet
            print(f'You drew, your betis returned, balance is {self.funddep}')
        elif self.splita == 'checkcheck':
            self.funddep += self.pbet
            print(f'You drew, a hand bet is returned, balance is {self.funddep}')
    
    def gbet(self):
        
        if self.funddep >= self.pbet:
            self.funddep -= self.pbet
            print(f'you have place a bet of {self.pbet}')
            print(f'you still have {self.funddep} availble for betting')
        else:
            print(f'you can not place any bet, you are low on fund. your balance is {self.funddep}')
    def details (self):
        print(f'Player: {self.name}')
        return f'Account balance: {self.funddep}'
       
    def blackjack (self):
        if self.playersum == 21 and 'blackjack' == self.decision:
            print (f'{self.name} has blackjack')
            Gamerules.winn(self)
            Gameplay.endgame(self)
        else:
            print ('you do not have blackjack as sum of your card is not 21. Make another decision')
            Gameplay.decisions (self)
    def surrender (self):
        if 'surrender' == self.decision:
            print (f'{self.name} has surrendered')
            Gamerules.half(self)
    def split (self):
        if 'split' == self.decision and self.cardn[0] == self.cardn[1] and len(self.cardn1) == 0 :
            if self.funddep >= 2*self.pbet:
                self.funddep -= self.pbet
                print (f'{self.name} has splited card ')
                self.cardn1.append(self.cardn[0])
                self.cardn2.append(self.cardn[1])
                print(f'you have place an extra bet of {self.pbet}')
                print(f'you still have {self.funddep} availble for betting')
                self.cardn1.append(self.deckcards[self.gamecount])
                self.gamecount +=1
                self.cardn2.append(self.deckcards[self.gamecount])
                self.gamecount +=1
                print(f'{self.name} here are your 2 sets of cards: Hand 1 {self.cardn1} and Hand 2 {self.cardn2}')
                choice = int(input('which hand do you want to focus on 1 or 2 ? '))
                for op in [1,2]:
                    if choice == 1:
                        print('You are now focusing in hand 1')
                        self.splita='checkcheck'
                        self.playersum = sum(self.cardn1)
                        self.cardn = self.cardn1
                        Gameplay.cvalues(self)
                        Gameplay.checkstatus1 (self)
                        if self.splitas == 'roll':
                            choice = 2
                            continue
                        Gameplay.decisions (self)
                        Gameplay.cvalues(self)
                        choice = 2
                        self.cardnh1 = self.cardn
                    elif choice ==2:
                        print('You are now focusing in hand 2')
                        self.splita='checkcheck'
                        self.playersum2 = sum(self.cardn2)
                        self.cardn2 = self.cardn2
                        Gameplay.cvalues(self)
                        Gameplay.checkstatus1 (self)
                        if self.splitas == 'roll':
                            choice = 1
                            continue
                        Gameplay.decisions (self)
                        Gameplay.cvalues(self)
                        choice = 1
                        self.cardnh2 = self.cardn
            else:
                print(f'You can not split, you are low on fund. your balance is {self.funddep} make another decision')
                Gameplay.decisions (self)
        else:
            print('Both cards do not have same values- also you can only split or double the first two cards. Make another decision')
            Gameplay.decisions (self)
    def double (self):
        if 'double' == self.decision and len(self.cardn) <=2 :
            if self.funddep >= 2*self.pbet:
                self.funddep -= self.pbet
                print(f'you have place an extra bet of {self.pbet}')
                print(f'you still have {self.funddep} availble for betting')
                self.cardn.append(self.deckcards[self.gamecount])
                print (f'you have drawn card: {self.deckcards[self.gamecount]}')
                self.gamecount +=1
            else:
                print(f'You can not place an extra bet, you are low on fund. your balance is {self.funddep}. Make another decision')
                Gameplay.decisions (self)
        else:
            print('You can only split or double the first two cards. Make another decision')
            Gameplay.decisions (self)

    def stand(self):
        if self.decision == 'stand':
            print (f'{self.name} has decided to stand ')
    def hit (self):
        if self.decision == 'hit':
            self.cardn.append(self.deckcards[self.gamecount])
            print (f'you have drawn card: {self.deckcards[self.gamecount]}')
            self.gamecount +=1
        
   


class Gameplay(Gamerules):
    def __init__(self):
        self.cardn =[]
        self.dealern =[]
        self.cardn1=[]
        self.cardn2=[]
        self.gamecount=0
        self.dealersum = sum(self.dealern)
        self.playersum = sum(self.cardn)     
        self.end =''
        self.name = input('Please enter your name: ')
    def start (self):
        self.decision=''
        self.cardnh1 =[]
        self.cardnh2 = []
        self.splita='notcheck'
        self.splitas = 'ntrolls'
        Gamerules.instructions(self)
        Gamerules.carddeck(self)
        self.deckcards=self.deck4
        self.funddep = int(input('Enter the total amount you have available for playing the game: '))

    def bet (self):
        
        self.pbet = int(input('Enter your bet for this round: '))
        from IPython.display import clear_output
        clear_output()
        Gamerules.gbet(self)
    def distribute (self):
        
        self.cardn =[]
        self.dealern =[]
        self.cardn1=[]
        self.cardn2=[]
        self.gamecount=0
        for i in [1,2]:
            self.cardn.append(self.deckcards[self.gamecount])
            self.gamecount +=1
            self.dealern.append(self.deckcards[self.gamecount])
            self.gamecount +=1
        print(f'{self.name} here are your cards: {self.cardn}')
        print(f'This is one of the dealers card: {self.dealern[0]}')
    def distributedealer (self):
        dist = True
        self.dealersum = sum(self.dealern)
        while dist:
            if self.dealersum <= 16:
                self.dealern.append(self.deckcards[self.gamecount])
                Gameplay.cvalues(self)
                self.gamecount +=1
                self.dealersum = sum(self.dealern)
                if self.dealersum >= 16:
                    dist= False
                    break
            else:
                dist= False
                break
        Gameplay.cvalues(self)
    def cvalues (self):
        self.carddict = {'Jack':10, 'Queen': 10, 'King': 10, 'Ace':[1,11]}
        facecard =['Jack','Queen','King','Ace']
        dealercard=0
        for ii in range(0,len(self.cardn)):
            for fc in facecard:
                if fc == 'Ace' and fc in self.cardn:
                    adecide= int(input('What value do you want your Ace card to be 1 or 11 ? '))
                    self.cardn.remove(fc)
                    self.cardn.append(adecide)
                elif fc != 'Ace' and fc in self.cardn:
                    self.cardn.remove(fc)
                    self.cardn.append(self.carddict[fc])
        for jj in range(0,len(self.dealern)):
            for kk in self.dealern:
                if isinstance(kk, int):
                    dealercard +=kk
            for fc in facecard:
                if fc == 'Ace' and fc in self.dealern:
                    if dealercard <= 10:
                        self.dealern.remove(fc)
                        self.dealern.append(11)
                    elif dealercard > 10:
                        self.dealern.remove(fc)
                        self.dealern.append(1)
                elif fc != 'Ace' and fc in self.dealern:
                    self.dealern.remove(fc)
                    self.dealern.append(self.carddict[fc])
                    
    def checkstatus1 (self):
        self.end =''
        self.dealersum = sum(self.dealern)
        self.playersum = sum(self.cardn)
        if self.dealersum == 21 and self.playersum != 21:
            print (f'Dealer has blackjack 21, Dealer wins the game with {self.dealersum}')
            self.end = 'ender'
            if self.splita != 'checkcheck': 
                Gameplay.endgame(self)
            elif self.splita == 'checkcheck':
                self.splitas = 'roll'
        elif self.playersum == 21 and self.dealersum != 21:
            print (f'Blackjack {self.name} wins the game with {self.playersum}')
            self.end = 'ender'
            Gamerules.winn(self)
            if self.splita != 'checkcheck': 
                Gameplay.endgame(self)
            elif self.splita == 'checkcheck':
                self.splitas = 'roll'
        elif self.playersum == 21 and self.dealersum == 21:
            print (' Game is a draw ')
            self.end = 'ender'
            Gamerules.dcredit(self)
            if self.splita != 'checkcheck': 
                Gameplay.endgame(self)
            elif self.splita == 'checkcheck':
                self.splitas = 'roll'
    def checkstatus (self):
        self.end =''
        self.dealersum = sum(self.dealern)
        self.playersum = sum(self.cardn)
        if self.dealersum > 21 and self.playersum <21:
            print (f'Dealer busrted {self.name} wins the game with {self.playersum}')
            self.end = 'ender'
            if self.splita != 'checkcheck': 
                Gameplay.endgame(self)
        elif self.playersum > 21 and self.dealersum <21:
            print (f'{self.name} busrted, Dealer wins the game with {self.dealersum}')
            self.end = 'ender'
            if self.splita != 'checkcheck': 
                Gameplay.endgame(self)
        elif self.dealersum > self.playersum and self.dealersum <= 21:
            print (f'Dealer wins the game with {self.dealersum}')
            self.end = 'ender'
            if self.splita != 'checkcheck': 
                Gameplay.endgame(self)
        elif self.dealersum < self.playersum and self.playersum <= 21:
            print (f'{self.name} wins the game with {self.playersum}') 
            self.end = 'ender'
            if self.splita != 'checkcheck': 
                Gameplay.endgame(self)
        elif self.dealersum == self.playersum and self.playersum <= 21:
            if len(self.dealern) > len(self.cardn):
                print (f'{self.name} wins the game with {self.playersum}')
                self.end = 'ender'
                if self.splita != 'checkcheck': 
                    Gameplay.endgame(self)
            elif len(self.dealern) < len(self.cardn):
                print (f'Dealer wins the game with {self.dealersum}')
                self.end = 'ender'
                if self.splita != 'checkcheck': 
                    Gameplay.endgame(self)
            elif len(self.dealern) == len(self.cardn):
                print ('The game is a draw!')
                self.end = 'ender'
                if self.splita != 'checkcheck': 
                    Gameplay.endgame(self)
    def decisions (self):
        print ('Here are your options')
        print ('blackjack, surrender, split, double, stand, hit ... Note you cannot split more than once ')
        self.decision = input('Pls input you decision here: ')
        if 'blackjack' == self.decision:
            Gamerules.blackjack(self)
        elif 'surrender' == self.decision:
            Gamerules.surrender(self)
            self.end = 'ender'
            Gameplay.endgame(self)
        elif 'split' == self.decision:
            Gamerules.split(self)
            Gameplay.distributedealer(self) 
            self.hand = 1
            for sp in [1,2]:
                if self.hand == 1:
                    self.cardn = self.cardnh1
                    Gameplay.checkstatus(self)
                    self.hand+=1
                elif self.hand == 2:
                    self.cardn = self.cardnh2
                    Gameplay.checkstatus(self)
                    self.hand+=1
            self.end = 'ender'
            Gameplay.endgame(self)
        elif 'double' == self.decision:
            Gamerules.double(self)
            Gameplay.cvalues(self)
        elif 'stand' == self.decision:
            Gamerules.stand(self)
        elif 'hit' == self.decision:
            Gamerules.hit(self)
            Gameplay.cvalues(self)
        else:
            print ('wrong input, make sure its the correct word in lower case')
            Gameplay.decisions(self)
    #def splitgame(self):
       # if self.decision == 'split':

    def endgame (self):
        self.endt=True
        if self.end == 'ender':
            lasttime=input('Do you wnat to end game Y/N : ')
            if lasttime =='Y':
                print('Thanks Goodbye')
                return
            
            elif lasttime == 'N':
                Gameplay.play(self)
    def play (self):
        self.endt=False
        Gameplay.start (self)
        Gameplay.bet (self)
        Gameplay.distribute (self)
        Gameplay.cvalues (self)
        Gameplay.checkstatus1 (self)
        Gameplay.decisions (self)
        if self.endt== False:
            Gameplay.distributedealer (self)
            Gameplay.checkstatus (self)
        elif self.endt== True:
            return


blckjck=Gameplay()
blckjck.play()