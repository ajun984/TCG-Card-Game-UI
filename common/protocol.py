from enum import Enum


class CustomProtocol(Enum):
    ACCOUNT_REGISTER = 1
    ACCOUNT_LOGIN = 2

    SESSION_LOGIN = 3

    DECK_NAME_LIST = 11
    ENTER_MATCHING = 12
    CHECK_MATCHING = 13
    DECK_CARD_LIST = 14

    PROGRAM_EXIT = 4444

class TypeProtocol(Enum):
    UNIT = 1
    ITEM = 2
    TRAP = 3
    SUPPORT = 4
    TOOL = 5
    ENERGY = 6
    ENVIRONMENT = 7
    TOKEN = 8



