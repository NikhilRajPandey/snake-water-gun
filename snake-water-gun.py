#  Sanke Water Gun Game

import  random, datetime
print('################Snake Water Gun#########################')
def wingame(you,comp):
    if comp==you:
        return None
    elif comp=='s':
        if you=='w':
            return False
        elif you=='g':
            return True,
    elif comp=='w':
        if you=='g':
            return False
        elif you=='s':
            return True
    elif comp=='g':
        if you=='s':
            return False
        elif you=='w':
            return True
i=0
score=0
while(i==0):

    ra= random.randint(1,3)
    if ra == 1:
        comp='s'
    elif ra == 2:
        comp='w'
    elif ra == 3:
        comp='g'

    print('Computer Turn: Snake(s) Water(w) Gun(g)?')
    you=input('Your Turn: Snake(s) Water(w) Gun(g)?')
    print(f'Computer Chose {comp}')
    print(f'You Chose {you}')

    if wingame(you, comp)== None:
        print('Tie')
        
    elif wingame(you,comp):
        print('You Win!!')
        score=5+score
        print(score)
        with open('score.txt','r') as f:
                d=f.readline()
        if d=='':
            with open('score.txt','w') as f:
                f.write(str(score))
        elif int(d)<int(score):
            with open('score.txt','w') as f:
                f.write(str(score))

    else:
        print('You Lose!!')
    i=int(input('Continue(0) Exit(1)?'))



x = datetime.datetime.now()
with open('score.txt','a') as f:
    f.write(f'\n{str(x)}')

