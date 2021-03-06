from typing import Any, Final

from src.views import GameView as GameViewBase
from src.views.console import console


class GameView(GameViewBase):
    START: Final = '\n-- Starting new game --\n'
    SCORE: Final = 'Player {} has {} points'

    @classmethod
    def show_start(cls) -> None:
        console.show(cls.START)

    @classmethod
    def show_score(cls, turn: Any) -> None:
        for player in turn["players"]:
            console.show(cls.SCORE.format(player['color'], player['score']))
