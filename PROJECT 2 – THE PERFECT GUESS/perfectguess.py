import random
class PERFECT_GUESS:
    def __init__(self,guessed_num):
        self._guessed_num=guessed_num
        
    @property
    def guessed_num(self):
        return self._guessed_num    
    
    guessed_num.setter
    def guessed_num(self,value):
        self._guessed_num=value
        
    def GUESSING(self):
        self._actual_num=random.randint(1,11)
        num_of_guesses=0
        process=True
        while process:     
          num_of_guesses+=1  
          if self._guessed_num>self._actual_num:
            print("Lower number please")
            self._guessed_num=int(input("guess the number"))
          elif self._guessed_num<self._actual_num:
            print("higher number please")
            self._guessed_num=int(input("guess the number"))
          else:
            print(f"the number of guesses the player used to arrive at the number{num_of_guesses}")  
            process=False  
            
a=PERFECT_GUESS(8)          
a.GUESSING()  