from enum import Enum

class Period(Enum):
    WINTER = 0
    SPRING = 1
    SUMMER = 2
    
    def __str__(self):
        return f"20{self.value}"
