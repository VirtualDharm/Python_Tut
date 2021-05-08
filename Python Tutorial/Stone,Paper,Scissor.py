import random
def game(a,b):
    if a==b:
        return None
    elif a=='s':
        if b=='p':
            return False
        elif b=='x':
            return True
    elif a=='p':
        if b=='x':
            return False
        elif b=='s':
            return True
    elif a=='x':
        if b=='s':
            return False
        elif b=='p':
            return True

a=input("Your turn| Stone(s),Paper(p) or Scissor(x):")
print("Comp turn| ")   
mylist = ('s','p','x') 
b=random.choice(mylist)
r=game(a,b)
print(f"You choose{a}: ")
print(f"Computer choose{b}: ")
if r ==None:
    print("The game is tie")
elif r==True:
    print("You win!")
elif r==False:
    print("You Lose!")