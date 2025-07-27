from rich.layout import Layout
from rich.console import Group, group
from rich.panel import Panel
from rich.console import Console
from rich.columns import Columns
from rich import print


console = Console()

# Setup table
game_layout = Layout()
game_layout.split_column(
    Layout(name="upper"),
    Layout(name="lower")
)

upper_group = Columns(
    [
        Panel("",title="Deck"),
        Panel("Card1\nCard2", title="Dealer Hand")
    ]
)


player_list = [
    "Ape",
    "Dog",
    "Orange"
]

player_group = Columns(
    [
        Panel(
            Panel("Card1\nCard2", title="Hand"),  # Inner panel for cards
            title=player
        )
        for player in player_list
    ]
)

game_layout["upper"].update(upper_group)
game_layout["lower"].update(player_group)
console.print(game_layout)

