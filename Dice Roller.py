import random


def dice_roll_1d6():
    print("Rolling 1d6.....")
    result = random.randint(1, 6)
    print("You rolled: ", result)
    return result


def dice_roll_1d8():
    print("Rolling 1d8.....")
    result = random.randint(1, 8)
    print("You rolled: ", result)
    return result


def dice_roll_1d20():
    print("Rolling 1d20.....")
    result = random.randint(1, 20)
    print("You rolled: ", result)
    return result


#  Menu Function that displays available options
def show_menu():
    print("Which die do you want to roll?")
    print("     A. 1d6")
    print("     B. 1d8")
    print("     C. 1d20")
    print("     D. View previous rolls")
    print("     Q. Quit program")
    print("")


# Function gets the user's choice
def get_user_choice():
    choice = input("Select a option: ").lower()
    return choice


def main():
    print("Dice roll sim")
    roll_list = []
    show_menu()
    menu_choice = get_user_choice()

    while menu_choice != 'q':
        if menu_choice == 'a':
            result = dice_roll_1d6()        # record roll to variable
            roll_list.append(result)        # record roll to previous roll list
        elif menu_choice == 'b':
            result = dice_roll_1d8()
            roll_list.append(result)
        elif menu_choice == 'c':
            result = dice_roll_1d20()
            roll_list.append(result)
        elif menu_choice == 'd':
            print("Previous rolls where: ")
            print(*roll_list, sep=", ")

        else:
            # Invalid option protection
            print("Invalid option, try again.")

        show_menu()
        menu_choice = get_user_choice()


main()
