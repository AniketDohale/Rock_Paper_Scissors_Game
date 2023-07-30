import random

choices = ['Rock', 'Paper', 'Scissor']

title = "Rock Paper Scissors"

print("---------------------------------------------------------------")
print("Winning Rules of the Game {} are :".format(title.upper()))
print("Rock vs Paper -> PAPER Wins")
print("Rock vs Scissors -> ROCK WinS")
print("Paper vs Scissors -> SCISSOR Wins")
print("---------------------------------------------------------------")


def start_game():
    while True:

        # User Choice
        user_choice = input(
            "Choice -> 'Rock' | 'Paper' | 'Scissor' \n").capitalize()

        if user_choice == 'Rock' or user_choice == 'Paper' or user_choice == 'Scissor':
            print("User Choice is", user_choice)
        else:
            print("Invalid User Input")
            print("Try Again..")
            start_game()
        print("---------------------------------------------------------------")

        print("Now its Computers Turn..")
        print("---------------------------------------------------------------")

        # Computer Choice
        comp_choice = random.choice(choices)
        print("Computer Choice is", comp_choice)
        print("---------------------------------------------------------------")

        print(user_choice, "VS", comp_choice)
        print("---------------------------------------------------------------")

        if user_choice == comp_choice:
            print("Match is DRAW..")
        elif user_choice == 'Rock' and comp_choice == 'Paper':
            print("Computer Wins..")
        elif user_choice == 'Paper' and comp_choice == 'Rock':
            print("User Wins..")
        elif user_choice == 'Scissor' and comp_choice == 'Paper':
            print("User Wins..")
        elif user_choice == 'Scissor' and comp_choice == 'Rock':
            print("Computer Wins..")
        elif user_choice == 'Rock' and comp_choice == 'Scissor':
            print("User Wins..")
        elif user_choice == 'Paper' and comp_choice == 'Scissor':
            print("Compter Wins..")

        print("---------------------------------------------------------------")
        play_again = input("Play Again (Yes/No) -> ")

        if play_again.capitalize() == 'No':
            print("Thanks for Playing..")
            break


start_game()
