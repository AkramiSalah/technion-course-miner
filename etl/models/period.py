from enum import Enum

class Period(Enum):
    WINTER = 1
    SPRING = 2
    SUMMER = 3
    
    def __str__(self):
        return f"20{self.value}"
