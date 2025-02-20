#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      chyas
#
# Created:     12/02/2025
# Copyright:   (c) chyas 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------
def intro():
    print("Welcome to the Dungeon Adventure Game!")
    print("You find yourself standing at the entrance of a dark dungeon.")
    print("Do you want to enter the dungeon? (yes/no)")

def first_choice():
    choice = input("Enter your choice: ").lower()

    if choice == "yes":
        print("You bravely step into the dungeon...")
        second_choice()
    elif choice == "no":
        print("You decide it's too dangerous and walk away.")
        end_game()
    else:
        print("Invalid choice, try again.")
        first_choice()

def second_choice():
    print("\nYou find yourself in a dark hallway. There are two doors ahead.")
    print("One door is cracked open, and you hear strange noises coming from it.")
    print("The other door is completely shut and silent.")
    print("Which door will you choose? (open/closed)")

    choice = input("Enter your choice: ").lower()

    if choice == "open":
        print("You open the door and are greeted by a giant spider!")
        fight_or_run()
    elif choice == "closed":
        print("You approach the closed door and cautiously open it. Inside is a treasure chest!")
        treasure_room()
    else:
        print("Invalid choice, try again.")
        second_choice()

def fight_or_run():
    print("\nThe spider lunges at you!")
    print("Do you fight the spider or run away? (fight/run)")

    choice = input("Enter your choice: ").lower()

    if choice == "fight":
        print("You bravely fight the spider and win! Congratulations!")
        end_game()
    elif choice == "run":
        print("You run away and escape the dungeon. Maybe next time...")
        end_game()
    else:
        print("Invalid choice, try again.")
        fight_or_run()

def treasure_room():
    print("\nInside the room, you find a treasure chest.")
    print("Do you want to open the chest? (yes/no)")

    choice = input("Enter your choice: ").lower()

    if choice == "yes":
        print("You open the chest and find gold and a magical sword!")
        print("Congratulations, you are now rich and powerful!")
        end_game()
    elif choice == "no":
        print("You decide not to open the chest. Maybe another time.")
        end_game()
    else:
        print("Invalid choice, try again.")
        treasure_room()

def end_game():
    print("\nGame Over! Thanks for playing.")
    play_again = input("Do you want to play again? (yes/no): ").lower()

    if play_again == "yes":
        intro()
        first_choice()
    elif play_again == "no":
        print("Goodbye!")
    else:
        print("Invalid choice, please enter 'yes' or 'no'.")
        end_game()

# Start the game
intro()
first_choice()
