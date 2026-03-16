class CourseQuery:
    def __init__(self, course_id, course_year, course_period):
        self.course_id     = course_id 
        self.course_year   = course_year 
        self.course_period = course_period 
    
    def __str__(self):
        return f"SmObjectSet(Otjid='SM{self.course_id}',Peryr='{self.course_year}',Perid='{self.course_period}',ZzCgOtjid='',ZzPoVersion='',ZzScOtjid='')"

