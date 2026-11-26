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

def create_clues():
    return [
        "Security footage shows Sarah in the living room near the safe",
        "A neighbor confirms Mike was outside during the incident",
        "The television was off, contradicting Alex's statement"
    ]

def display_clues(clues):
    print("\nCLUES")
    for i, clue in enumerate(clues, 1):
        print(f"{i}. {clue}")

def get_clues_for_suspect(clues, suspect):
    if suspect == "Sarah":
        return [clues[0]]
    elif suspect == "Mike":
        return [clues[1]]
    elif suspect == "Alex":
        return [clues[2]]
    else:
        return []
