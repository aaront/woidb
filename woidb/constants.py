from enum import Enum


class GameStatus(Enum):
    not_started = 0
    finished = 3


class EventType(Enum):
    block = 0
    goal = 1
    miss = 2
    shot = 3
    faceoff = 4
    giveaway = 5
    takeaway = 6
    penalty = 7
    hit = 8
    stop = 9
    periodend = 10


class EventZone(Enum):
    defensive = 0
    offensive = 1
    neutral = 2
