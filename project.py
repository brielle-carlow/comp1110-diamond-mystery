def get_player_choice():
    """
    Ask the player to enter the name of the suspect.
    """
    choice = input("Who do you think stole the necklace? ")
    return choice
    
def check_answer(player_choice, correct_suspect):
    """
    Check whether the player's chosen suspect is correct.
    """
    if player_choice.lower() == correct_suspect.lower():
        return True
    else:
        return False

def display_result(is_correct, correct_suspect):
    """
    Display whether the player solved the mystery.
    """
    if is_correct:
        print("Congratulations! You solved the mystery!")
    else:
        print("CASE UNSOLVED. Sorry! That is not the correct suspect. You accused the wrong person.")
        print("The necklace was stolen by", correct_suspect)

def main():
    """
    Run the necklace mystery game.
    """
    print("Welcome to The Missing Necklace!")
    print("There are three suspects. Can you figure out who stole the necklace?")

    correct_suspect = "Sarah" #PLACE HOLDER FIX NAME IF ITS DIFFERENT#

    player_choice = get_player_choice()

    is_correct = check_answer(player_choice, correct_suspect)

    display_result(is_correct, correct_suspect)


if __name__ == "__main__":
    main()
