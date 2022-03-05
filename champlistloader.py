from core import Champion


def _parse_champ(champ_text: str) -> Champion:
    name, rock, paper, scissors = champ_text.split(sep=',')
    return Champion(name, float(rock), float(paper), float(scissors))


def from_db(list_of_champions: list) -> dict[str, Champion]:
    champions = {}
    for champion in list_of_champions:
        name = champion['champion']
        rock = champion['rock']
        paper = champion['paper']
        scissors = champion['scissors']
        champions[name] = Champion(name, float(rock), float(paper), float(scissors))
    return champions

def load_some_champs():
    return from_csv('some_champs.txt')
