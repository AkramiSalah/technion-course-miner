from enum import Enum

class NavSegment(Enum):
    RELATIONS         = "SmRelations"
    RELATIONS_REVERSE = "SmRelationsReverse"
    PERIOD            = "SmOfferedPeriodSet"
    PREREQ            = "SmPrereq"
    
    def __str__(self):
        return f"/{self.value}"