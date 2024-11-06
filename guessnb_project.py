from random import*
def guessnb():
    n=0
    pseudo=input("What is your name?")
    print(f"-Hello {pseudo}\nWelcome to the Number Guessing Game \nI'm thinking a number between 1 and 100")
    print("-Please select the difficulty level: \n1. Easy (10 chances) \n2. Medium (5 chances) \n3. Hard (3 chances)")
    rep=input("Enter you choice (1-3)")
    if rep=="1":difficulty,chances="Easy",10
    elif rep=="2":difficulty,chances="Medium",5
    elif rep=="1":difficulty,chances="Hard",3
    else:chances=0
    print("You have selected the {difficulty} level\nLet's start the game")
    nb=randint(1,100)
    while chances>0:
        guess=eval(input("Enter your guess: "));n+=1;chances-=1
        if guess==nb:
            print(f"Congratulations! You guessed the correct number in {n} attempts\n")
            break
        elif guess>nb:print(f"Incorrect! The number is less than {guess}.\n")
        elif guess<nb:print(f"Incorrect! The number is greater than {guess}.\n")
    if chances==0:print(f"you haven't find the number after your chances, the number is {nb}.")
    
guessnb()