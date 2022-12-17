#simulador de pedra papel tisoura
import random

laso=bool(True)
while(laso):
   c=int(input('1 tessoura 2 pedra 3 papel'))
   b=random.randint(1,3)   
   if(c==b):
      print('voce jogou {}'.format(c))
      print('eu joguei {}'.format(b))
      print('voce ganho !!!!!')
   else:
      print('voce jogou {}'.format(c))
      print('eu joguei {}'.format(b))
      print('eu ganhei !!!!')
   d=input('que revanxi ')
   if(d=='sim'):
      print('===================================')
   if(d=='nao'):
      print('=============================')
      laso=False