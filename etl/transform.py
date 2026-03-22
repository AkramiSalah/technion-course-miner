def get_name(course_data):
    return course_data["Name"]

def get_syllabus(course_data):
    return course_data["StudyContentDescription"]

def get_points(course_data):
    return int(course_data["PointsMaximum"])

def get_course_id_8(course_data):
    return course_data["Otjid"][2:]

def get_course_id_6(course_data):
    long_format = get_course_id_8(course_data)
    lhs = long_format[1:3]
    rhs = long_format[4:]
    return lhs + rhs

def get_prereq_str(prereq_data):
    results = prereq_data["results"]
    
    def is_module(entry):
        return entry["ModuleId"] != "00000000"
    
    def get_course_str(entry):
        if is_module(entry):
            return f"{entry["ModuleName"]}({entry["ModuleShort"]})"
        return ""
    
    def formatted_entry(entry):
        return f"{entry["Bracket"]}{get_course_str(entry)}{entry["Operator"]}"
    
    prereq_str = ""
    for entry in results:
        prereq_str += (formatted_entry(entry))

    return prereq_str

def get_relations(relations_data):
    relations_dict  = {}
    for entry in relations_data["results"]:
        relationship = entry["ZzRelationship"]
        formatted_course_name = f'{entry["Name"]} ({entry["Short"]})'

        if relationship in relations_dict .keys():
            relations_dict [relationship].append(formatted_course_name)
        else:
            relations_dict [relationship] = [formatted_course_name]
    
    return relations_dict