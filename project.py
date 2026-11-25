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
