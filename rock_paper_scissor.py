'''
ROCK,PAPER,SCISSOR game against computer 
'''
import random
import os
os.system('cls')

class Game:

      def __init__(self):
            self.choices = {'R' : 'ROCK', 'P' : 'PAPER', 'S' : 'SCISSOR'}
            self.computer = random.choice(list(self.choices.keys()))
            self.user = None
            while True:
                  try:
                        self.user = input('Please Choose "R" for ROCK , "P" for PAPER and "S" for SCISSOR \n').upper()
                        if self.user not in self.choices:
                              print('OOPs thats Invalid choice !!!')
                              continue
                  except:
                        print('Something Went Wrong')

                  else:
                        break
      
      # r>s, s>p, p>r
      def winner(self):
            if self.user == self.computer:
                  print('DRAW !')
            elif self.user == 'R' and self.computer == 'S':
                  print(f'Congrats You WON ! \ncomputer was having {self.choices[self.computer]}')
            elif self.user == 'S' and self.computer == 'P':
                  print(f'Congrats You WON ! \ncomputer was having {self.choices[self.computer]}')
            elif self.user == 'P' and self.computer == 'R':
                  print(f'Congrats You WON ! \ncomputer was having {self.choices[self.computer]}')
            else:
                  print(f'You Lost to Computer \ncomputer was having {self.choices[self.computer]}')



while True:
      try:
            g = Game()
            g.winner()
            x = input('Play Again !! "Y" or "N" ? \n').upper()
            if x == 'Y' :
                  os.system('cls') 
                  continue
            else: print('Thankyou For Playing')                 
      except:
            print('Try Again')
      else:break
      