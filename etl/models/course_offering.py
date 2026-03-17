from dataclasses import dataclass

@dataclass
class CourseOffering:
    name          : str
    _id           : str
    prereqs       : str
    parallels     : str 
    no_extra_cred : str     
    syllabus      : str


