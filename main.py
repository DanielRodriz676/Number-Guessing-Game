import random

def choice():
    try:
        level = int(input("Enter your choice: "))
        if 0 < level < 4:
            return level
        print("numero inválido")
        return choice()
    except:
        print("valor inválido")
        return choice()

def guess():
    try:
        y_guess = int(input("Enter your guess: "))
        return y_guess
    except:
        print("valor inválido")
        return guess()

def verfy(num, result):
    if num > result:
        return print(f"Incorrect! The number is less than {num}.\n")
    elif num < result:
        return print(f"Incorrect! The number is greater than {num}.\n")
    return print(f"Congratulations! You guessed the correct number {result}.")

def main():
    print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.\n\nPlease select the difficulty level:\n1. Easy (10 chances)\n2. Medium (5 chances)\n3. Hard (3 chances)\n")

    r_number = random.choice(range(1, 100))
    level = choice()
    
    if level == 1:
        print("Great! You have selected the Easy difficulty level.\nLet's start the game!\n")
        level = 10
    elif level == 2:
        print("Great! You have selected the Medium difficulty level.\nLet's start the game!\n")
        level = 5
    else:
        print("Great! You have selected the Hard difficulty level.\nLet's start the game!\n")
        level = 3

    for a in range(level):
        p_guess = guess()
        verfy(p_guess, r_number)
        if p_guess == r_number:
            break

if __name__ == "__main__":
    main()
