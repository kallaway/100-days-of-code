import random
def gamewin(you,comp):
    if(you==comp):
        return None
    if you=='r':
        if comp=='s':
            return True 
        if comp=='p':
            return False
    if you=='p':
        if comp=='s':
            return False
        if comp=='r':
            return True
    if you=='s':
        if comp=='r':
            return False
        if comp=='p':
            return True
print("comp turn rock(r) paper(p) scissor(s)")
randno =random.randint(1,3)
if randno==1:
    comp='r'
elif randno==2:
    comp='p'
elif randno== 3:
    comp='s'       

you=input(" rock or paper or scissor ")
a=gamewin(you,comp)

print(f"computer chose {comp}  ")
print(f"you chose  {you}  ")

if a==None:
    print("tie")
elif a:
    print("you won")
else:
    print("you loser")
