def victim_statement(name, statement):
    print(f"{name}'s statement is \"{statement}\"")
print(victim_statement("Sarah", "I left my necklace on the night stand before i went shopping and when I returned it was no longer there"))
    
class Suspect:
    def __init__(self, name, job, statement):
        self.name = name
        self.job = job
        self.statement = statement

def create_suspects():
    merilin = Suspect("merilin", "hotel manager", "I was in my office doing paper work")
    brielle = Suspect("brielle", "guest", "I was relaxing by the pool")
    mehak = Suspect("mehak", "security", "i was patrolling around the lobby")
    return [merilin, brielle, mehak]

def display_suspects(suspects):
    for suspect in suspects:
        print(f"{suspect.name}, {suspect.job}, {suspect.statement}")

suspects = create_suspects()
display_suspects(suspects)
