class InvalidCourseID(Exception): pass

class CourseQuery:
    def __init__(self, course_id, course_year, course_period):
        self.course_id     = valid_id(course_id) 
        self.course_year   = course_year 
        self.course_period = course_period 
    
    def __str__(self):
        return f"SmObjectSet(Otjid='SM{self.course_id}',Peryr='{self.course_year}',Perid='{self.course_period}',ZzCgOtjid='',ZzPoVersion='',ZzScOtjid='')"


def valid_id(id):
    if len(id) > 8:
        raise InvalidCourseID("Invalid ID, has more than 8 chars!!!")

    if len(id) == 8:
        return id
    
    while len(id) < 7:
        id = '0' + id
    
    return id[0:4] + '0' + id[-3:]