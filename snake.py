import random
ra=random.randint(1,3)
def game(c,y):
    if c==y:
        print("tie")
    elif c=='s':
        if y=='w':
            print("you loose")
        elif y=='g':
            print("you won")
    elif c=='w':
        if y=='s':
            print("you loose")
        elif y=='g':
            print("you won")
            

    elif c=='g':
        if y=='s':
            print("you loose")
        elif y=='w':
            print("you won")

if ra==1:
    comp='s'
elif ra==2:
    comp='w'
elif ra==3:
    comp='g'
you=input("Yours  turn : snake(s) water(w) or gun(g)")
print(f'comp choose   {comp}')
print(f'you choose    {you}')
game(comp,you)
