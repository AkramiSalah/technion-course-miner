import json
import sys

VALID_ID_LENGTH = 6
EXTENDED_ID_LENGTH = 8

def sanitize(course_id):
    if(len(course_id) == VALID_ID_LENGTH):
        return course_id
    elif(len(course_id) == EXTENDED_ID_LENGTH):
        if(course_id[0] == '0' and course_id[4] == '0'):
            course_id = course_id[1:4] + course_id[5:]
            return course_id
    else:
        print(f"{course_id} is a bad course_id, its length isnt 6 or 8!!!", file=sys.stderr) 

    return "BAD_ID"

def load(course_ids_file_path):
    try:
        with open(course_ids_file_path, 'r') as f:
            raw_course_ids = json.load(f)["ids"]
            return [sanitize(course_id) for course_id in raw_course_ids]
    except (FileNotFoundError, KeyError) as e:
        print(f"Error loading {course_ids_file_path} : {e}")
        return None
