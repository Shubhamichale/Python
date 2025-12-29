def games():
    import random
    opponent=random.randint(1,3)
    select={
        1:"SNAKE",
        2:"WATER",
        3:"GUN"
    }
    option='''"CHOOSE ONE OF THESE OPTIONS:" :
1:"SNAKE",
2:"WATER",
3:"GUN"
    '''
    print(option)
    chosen=int(input("ENTER THE OPTION YOU CHOSE: "))
    print(f"YOU CHOSE {select.get(chosen)}")
    print(f"OPPONENT CHOSE {select.get(opponent)}")
    
    if((chosen==1 and opponent==2) or (chosen==2 and opponent==3) or (chosen==3 and opponent==1)):
        return 1
    elif(chosen==opponent):
        return 0
    else:
        return -1

def result(n):
    if(n==1):
        print("YOU WIN")
    elif(n==0):
        print("IT'S A DRAW!")
    else:
        print("OPPONENT WINS")

l = []
for i in range(5):
    print(f"\nROUND {i+1}")
    die = games()
    l.append(die)
    result(die)

print("\nGame Results:", l)

score = sum(l)
print("Your Total Score:", score)


with open("Hi-score.txt") as f:
    pre=f.read()

if(pre==""):
    pre="0"

if(score>int(pre)):
   print("New High Score!")
   pre=str(score)

with open("Hi-score.txt","w") as f:
    f.write(str(pre))
