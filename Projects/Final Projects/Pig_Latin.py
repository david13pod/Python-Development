from IPython.display import clear_output

class Gamer():
    def instruction(self):
        print('welcome to Pig Latin! It is simple,the first letter/syllable of any word you input would be moved '
             '\nto the end of the word and "ay" added to it. If the first letter is a vowel then, "way" is added.' 
             '\nMacht Spass!!!')
    def alphabet(self):
        self.letters=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        self.const=['B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Y','Z']
        self.vowels=['A','E','I','O','U']

class Play(Gamer):
    def __init__(self):
        self.output=''
        self.piglt=[]
        self.count=0
        self.waiting=[]
        
    def start(self):
        clear_output()
        Gamer.alphabet(self)
        Gamer.instruction(self)
        Play.proceed(self)
        Play.endgame(self)
    
    def proceed(self):
        inpt= input('Please enter your word ')
        upinpt= inpt.upper()
        self.inpt= upinpt.split()
        for x in self.inpt:
            self.count=0
            for iq in x:
                self.count+=1
                if iq in self.vowels and self.count==1 :
                    self.waiting= x.replace(iq,'')
                    self.kad=iq+'WAY'
                    self.output=self.waiting + self.kad
                    self.piglt.append(self.output)
                    break
                elif iq in self.const and self.count==1 :
                    self.waiting= x.replace(iq,'')
                    self.kad=iq+'AY'
                    self.output=self.waiting + self.kad
                    self.piglt.append(self.output)
                    break
                elif not iq in self.letters and self.count==1 :
                    
                    self.output=x
                    self.piglt.append(self.output)
                    break
        
        print ('Here is your output:')
        print (' '.join(self.piglt))
        
    def endgame(self):
        einpt= input('Do you want to play again? Y or N ')
        eupinpt= einpt.upper()
        if eupinpt == 'Y':
            Play.start(self)
            
        elif eupinpt == 'N':
            clear_output()
            print ('Thanks for playing Piglatin, Tschuss!')
                    
        
        
        
        
playing=Play()   
playing.start()
