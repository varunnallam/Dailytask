" write a program that generates a random  number between 1 to 100 , the program give hints to high and low until user guesses correctly "
n = int(input("Enter the guessing game: "))
guess = None  
print("selecte the guess in number between 1 to 100")
while guess != n:
    guess = int(input("Guess a number:"))
    if guess<1 and guess>100:
        print(" guess a number between 1 and 100.")
    elif guess > n:
        print("Too high!")
    elif guess < n:
        print("Too low!")
    else:
        print("Correct!")