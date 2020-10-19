from enum import Enum


class GameInternalState(Enum):
    NONE = 0,
    FIRST_CARD = 1,
    SECOND_CARD = 2,
    PLAYING = 3,