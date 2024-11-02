import random,os
from  game_data import data
from art import logo,vs


started=False
score=0
result=False
def play():
    global started
    if(started==False):
        started=True
        A=random.choice(data)
        B=random.choice(data)
        while(A==B):
            B=random.choice(data)
        return A,B
    else:
        C=random.choice(data)
        return C
    
    
def display(A,B):
    print(f"Compare A: {A['name']}, a {A['description']} from {A['country']}.")
    print(vs)
    print(f"Against B: {B['name']}, a {B['description']} from {B['country']}.")
    compare(A,B)
   
        
def compare(A,B):
    global score,result,BG
    choice=input("Who has more followers? Type 'A' or 'B':").lower()
    if(choice=='a'):
        choice=A
    else:
        choice=B
        
    if(A['follower_count']>B['follower_count']):
        famous=A
    else:
        famous=B

    if choice == famous:
        score+=1
        print(f"You're right! Current score: {score}\n")
        result= True
        BG=B
    else:
        print(logo)
        print(f"Sorry that's wrong. final Score: {score}")
        result= False
        

print(logo)
A,BG=play()
display(A,BG)
while(result):
    C=play()
    display(BG,C)
  
    
    

