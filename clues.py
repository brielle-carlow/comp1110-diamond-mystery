def create_clues():
    clues = [
        {"description": "Clue 1: Papers disturbed in the manager's office.", "points_to": "merilin"},
        {"description": "Clue 2: Wet footprints near the pool.", "points_to": "brielle"},
        {"description": "Clue 3: A security key found in the lobby.", "points_to": "mehak"},
    ]
    return clues

def display_clues(clues):
    print("\n--- Clues ---")
    for clue in clues:
        print(clue["description"])

def get_clues_for_suspect(clues, suspect_name):
    matching = []
    for clue in clues:
        if clue["points_to"].lower() == suspect_name.lower():
            matching.append(clue["description"])
    return matching