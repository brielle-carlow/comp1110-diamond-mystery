def create_clues():
    clues = [
        {"description": "Clue 1: A torn cleaning glove found near the bedroom door.", "points_to": "Elena"},
        {"description": "Clue 2: Muddy footprints in the garden, but none inside the house.", "points_to": "Marcus"},
        {"description": "Clue 3: A teacup in the living room is still warm.", "points_to": "Priya"}
    ]
    return clues

def display_clues(clues):
    print("\n--- CLUES FOUND ---")
    for clue in clues:
        print(clue["description"])

def get_clues_for_suspect(clues, suspect_name):
    result = []
    for clue in clues:
        if clue["points_to"].lower() == suspect_name.lower():
            result.append(clue["description"])
    return result
