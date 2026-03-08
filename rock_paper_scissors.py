
import random
while True:
    computer=random.randint(0,2)
    print('---')
    if computer==0:
      computer='rock'
    if computer==1:
      computer='paper'
    if computer==2:
      computer='scissors'
    num=input('you choose rock,paper or scissors? ')

    print('computer chooses:', computer)
    print('---')
    if num==computer:
      print('draw')
    else:
        if computer=='rock':
          if num=='paper':
            print('you win !!')
          elif num=='scissors':
            print('you lose ;(')

        elif computer=='paper':
          if num=='rock':
            print('you lose ;(')
          elif num=='scissors':
            print('you win !!')  

        elif computer=='scissors':
          if num=='paper':
              print('you lose ;(')
          elif num=='rock':
              print('you win !!') 
    choi_tiep=input('wanna play again? (yes/no)')
    if choi_tiep!='yes':
       break
        
        

                    