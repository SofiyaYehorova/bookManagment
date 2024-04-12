from enum import Enum


class Regex(Enum):
    NAME = (
        r'^[a-zA-Z\d]{,24}$',
        'min 1 max 25 ch'
    )
    AUTHOR = (
        # r'^[a-zA-Z]{1,100}$',
        r'^\S+(\s+\S+){1,99}$',
        'Only alphabetical characters are allowed, min 2 max 100 characters'
    )
    ISBN = (
        r'^[a-zA-Z\d\-]{10,20}$',
        'min 10 max 20 characters'
    )

    def __init__(self, pattern: str, msg: str):
        self.pattern = pattern
        self.msg = msg
