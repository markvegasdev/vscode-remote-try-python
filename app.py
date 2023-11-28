#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")


# create a main def
def main():
    score = 0
    number_of_games = 0
    print("================================")
    print("  Rock, Paper o Scissors GAME")
    print("================================")
    rules()
    user_option = user_choice()
    computer_option = computer_choice()
    print("================================")
    result = compare(user_option, computer_option)
    calculate_score(result, score, number_of_games)
    print("================================")
    while True:
        play_again = input("Do you want to play again? (y/n): ")
        if play_again == "y":
            user_option = user_choice()
            computer_option = computer_choice()
            print("================================")
            calculate_score(compare(user_option, computer_option), score, number_of_games)
            print("================================")
        elif play_again == "n":
            print("Thanks for playing!")
            break
        else:
            print("Invalid option. Please try again.")
            continue

    

def rules():
    print("Rules of the Game:")
    print("Rock beats Scissors")
    print("Scissors beats Paper")
    print("Paper beats Rock")
    print("================================")

def user_choice():
    print("Choose one of the following options:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("================================")
    user_choice = int(input("Enter your choice: "))
    print("User chose: " + option_to_string(user_choice))
    return user_choice

def generate_random_number():
    import random
    random_number = random.randint(1, 3)
    return random_number

def computer_choice():
    computer_choice = generate_random_number()
    print("Computer chose: " + option_to_string(computer_choice))
    return computer_choice

def option_to_string(option):
    if option == 1:
        return "Rock"
    elif option == 2:
        return "Paper"
    elif option == 3:
        return "Scissors"
    else:
        return "Invalid option. Please try again."

def calculate_score(flag, score, number_of_games):
    if flag == 1:
        score += 1
        number_of_games += 1
    elif flag == -1:
        number_of_games += 1
    elif flag == 0 | flag == -100:
        number_of_games
    else:
        print("Invalid flag. Please try again.")

    print("Score: " + str(score) + "/" + str(number_of_games))
    return score, number_of_games

def compare(user_option, computer_option):
    print("user:" + option_to_string(user_option) + " vs computer:" + option_to_string(computer_option))
    if user_option == 1:
        if computer_option == 1:
            print("It's a tie!")
            return 0
        elif computer_option == 2:
            print("Computer wins!")
            return -1
        elif computer_option == 3:
            print("You win!")
            return 1
    elif user_option == 2:
        if computer_option == 1:
            print("You win!")
            return 1
        elif computer_option == 2:
            print("It's a tie!")
            return 0
        elif computer_option == 3:
            print("Computer wins!")
            return -1
    elif user_option == 3:
        if computer_option == 1:
            print("Computer wins!")
            return -1
        elif computer_option == 2:
            print("You win!")
            return 1
        elif computer_option == 3:
            print("It's a tie!")
            return 0
    else:    
        print("Invalid option. Please try again.")
        return -100



            


if __name__ == "__main__":
    app.run(main())
