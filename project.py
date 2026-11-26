def main():
    """
    Run the necklace mystery game.
    """
    print("Welcome to The Missing Necklace!")
    print("There are three suspects. Can you figure out who stole Sarah's necklace?")

    correct_suspect = "Merilin"

    player_choice = get_player_choice()

    is_correct = check_answer(player_choice, correct_suspect)

    display_result(is_correct, correct_suspect)

if __name__ == "__main__":
    main()
#merilin work
class Suspect:
    def __init__(self, name, job, statement):
        self.name = name
        self.job = job
        self.statement = statement

def create_suspects():
    """Creates a list of suspects with their names, jobs, and statements."""
    merilin = Suspect("merilin", "hotel manager", "I was in my office doing paper work")
    brielle = Suspect("brielle", "guest", "I was relaxing by the pool")
    mehak = Suspect("mehak", "security", "i was patrolling around the lobby")
    return [merilin, brielle, mehak]

def display_suspects(suspects):
    """Displays the list of suspects with their details."""
    for suspect in suspects:
        print(f"{suspect.name}, {suspect.job}, {suspect.statement}")

suspects = create_suspects()
display_suspects(suspects)

#brielle work
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
    return play_choice.strip().lower()==correct_suspect.strip().lower()

def display_result(is_correct, correct_suspect):
    """
    Display whether the player solved the mystery.
    """
    if is_correct:
        print("Congratulations! You solved the mystery!")
    else:
        print("CASE UNSOLVED. Sorry! That is not the correct suspect. You accused the wrong person.")
        print("The necklace was stolen by", correct_suspect)
