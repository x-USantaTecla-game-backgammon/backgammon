from typing import Final

from src.views import console


class MatchView:
    TITLE: Final = '### BACKGAMMON ###'
    CHOOSE_COLOR: Final = 'Each player should choose a color.'
    DEFINE_GOAL: Final = 'Define your goal?'
    GOAL_RANGE: list[int] = list(range(1, 64))
    RESUME: Final = 'Do you want to resume a match?'

    @classmethod
    def show(cls) -> None:
        console.show(
            f'{cls.TITLE}\n\n'
            f'{cls.CHOOSE_COLOR}\n\n'
        )

    @classmethod
    def read_goal(cls) -> int:
        return console.read_int_range(valids=cls.GOAL_RANGE, msg=cls.DEFINE_GOAL)

    @classmethod
    def read_resume(cls) -> bool:
        return console.read_bool(cls.RESUME)