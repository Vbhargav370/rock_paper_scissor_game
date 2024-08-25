import random 
print("Rock, Paper, Scissor....")
game = ['Rock', 'Paper','Sciccor']
user = int(input("Enter Your Choice 0 is Rock, 1 is Paper, 2 for Sciccor...! : "))
computer = random.randint(0,2)
if user >=0 and user <=2:
    print(f"You chose {game[user]}, Computer chose {game[computer]}.")
    if user == computer:
        print("The Game is drawn ....")
    elif (user == 1 and computer == 0) or (user == 0 and computer == 2) or (user == 2 and computer == 1):
        print(" You Win the Game... 😘🥳🥳🥳")
    else:
        print("Computer Wins the Game ... 😝")    
else:
    print("The Value You Entered out of Bound")