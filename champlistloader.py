from core import Champion

def from_db(list_of_champions: list) -> dict[str, Champion]:
    champions = {}
    for champion in list_of_champions:
        name = champion['champion']
        rock = champion['rock']
        paper = champion['paper']
        scissors = champion['scissors']
        champions[name] = Champion(name, float(rock), float(paper), float(scissors))
    return champions
