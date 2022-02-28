from rich import print
from rich.prompt import Prompt
from rich.table import Table
from rich.console import Console

from champlistloader import load_some_champs
from core import Champion, Match, Shape, Team


def print_available_champs(champions: dict[Champion]) -> str: 

    # Create a table containing available champions
    available_champs = Table(title='Available champions')

    # Add the columns Name, probability of rock, probability of paper and
    # probability of scissors
    available_champs.add_column("Name", style="cyan", no_wrap=True)
    available_champs.add_column("prob(:raised_fist-emoji:)", justify="center")
    available_champs.add_column("prob(:raised_hand-emoji:)", justify="center")
    available_champs.add_column("prob(:victory_hand-emoji:)", justify="center")

    # Populate the table
    for champion in champions.values():
        available_champs.add_row(*champion.str_tuple)

    console = Console(record = True)
    console.print(available_champs)
    string = console.export_text()
    return string

def input_champion(name: str,
                   champions: dict[Champion],
                   player1: list[str],
                   player2: list[str]) -> bool:
    match name:
        case name if name not in champions:
            print(f'The champion {name} is not available. Try again.')
            return True
        case name if name in player1:
            print(f'{name} is already in your team. Try again.')
            return True
        case name if name in player2:
            print(f'{name} is in the enemy team. Try again.')
            return True
        case _:
            player1.append(name)
            return False

def print_match_summary(match: Match) -> None:

    console = Console(record = True)

    EMOJI = {
        Shape.ROCK: ':raised_fist-emoji:',
        Shape.PAPER: ':raised_hand-emoji:',
        Shape.SCISSORS: ':victory_hand-emoji:'
    }

    # For each round print a table with the results
    for index, round in enumerate(match.rounds):

        # Create a table containing the results of the round
        round_summary = Table(title=f'Round {index+1}')

        # Add columns for each team
        round_summary.add_column("Red",
                                 style="red",
                                 no_wrap=True)
        round_summary.add_column("Blue",
                                 style="blue",
                                 no_wrap=True)

        # Populate the table
        for key in round:
            red, blue = key.split(', ')
            round_summary.add_row(f'{red} {EMOJI[round[key].red]}',
                                  f'{blue} {EMOJI[round[key].blue]}')
        console.print(round_summary)
        console.print('\n')

    # Print the score
    red_score, blue_score = match.score
    console.print(f'Red: {red_score}\n'
          f'Blue: {blue_score}')

    # Print the winner
    if red_score > blue_score:
        console.print('\n[red]Red victory! :grin:')
    elif red_score < blue_score:
        console.print('\n[blue]Blue victory! :grin:')
    else:
        console.print('\nDraw :expressionless:')

    string = console.export_text()
    return string


def play_match(champions, player1, player2) -> str:
    # Match
    match = Match(
        Team([champions[name] for name in player1]),
        Team([champions[name] for name in player2])
    )
    match.play()

    # Print a summary
    return print_match_summary(match)


if __name__ == '__main__':
    main()
