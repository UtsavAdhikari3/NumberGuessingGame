import random

def generate_random_num():
    return random.randrange(1,11)


def guess_num(choice):
    random_number = generate_random_num()

    if choice == 1:
        for i in range(10):
            guess_num = int(input("Enter your guess: "))
            if guess_num == random_number:
                print(f"Congratulations! You guessed the correct number in {i+1} attempts.")
                keep_playing = int(input("""Do you want to keep playing?
1. Yes
0. No: """))
                if keep_playing == 1:
                    main()
                break
            elif guess_num > random_number:
                print(f"Incorrect! The number is less than {guess_num}.")
            elif guess_num < random_number:
                print(f"Incorrect! The number is greater than {guess_num}.")

    elif choice == 2:
        for i in range(5):
            guess_num = int(input("Enter your guess: "))
            if guess_num == random_number:
                print(f"Congratulations! You guessed the correct number in {i+1} attempts.")
                keep_playing = int(input("""Do you want to keep playing?
1. Yes
0. No: """))
                if keep_playing == 1:
                    main()
                break
            elif guess_num > random_number:
                print(f"Incorrect! The number is less than {guess_num}.")
            elif guess_num < random_number:
                print(f"Incorrect! The number is greater than {guess_num}.")

    elif choice == 3:
        for i in range(3):
            guess_num = int(input("Enter your guess: "))
            if guess_num == random_number:
                print(f"Congratulations! You guessed the correct number in {i+1} attempts.")
                keep_playing = int(input("""Do you want to keep playing?
1. Yes
0. No: """))
                if keep_playing == 1:
                    main()
                break
            elif guess_num > random_number:
                print(f"Incorrect! The number is less than {guess_num}.")
            elif guess_num < random_number:
                print(f"Incorrect! The number is greater than {guess_num}.")
    else:
        print("Sorry but your choice is out of bounds.")


def main():
    print("""Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
You have 5 chances to guess the correct number.
          """)
    
    print("""Please select the difficulty level:
1. Easy (10 chances)
2. Medium (5 chances)
3. Hard (3 chances)""")
    
    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("""Great! You have selected the Easy difficulty level.
Let's start the game!""")
        guess_num(choice)
    elif choice == 2:
        print("""Great! You have selected the Medium difficulty level.
Let's start the game!""")
        guess_num(choice)
    
    else:
        print("""Great! You have selected the Hard difficulty level.
Let's start the game!""")
        guess_num(choice)


if __name__ == "__main__":
    main()