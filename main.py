import json
from etl.extract import *
from etl.transform import *
from etl.models import period
import time, random


def save(result_dict, output_path):
    with open(output_path, 'w') as out:
        json.dump(result_dict, out, indent=4)
    print(f"  Saved {len(result_dict)} courses.")


def main():
    path_to_raw_input = "data/raw/course_ids.json"


    year = '2025'
    season = period.Period.WINTER

    with open(path_to_raw_input) as f:
        raw_input = json.load(f)

    current_query = CourseQuery('12345678', year, season)

    result_dict = {}

    try:
        for i,id in enumerate(raw_input['ids']):
            print(i, id)
            current_query.set_course_id(id)
            general_data     = extract_course_general(current_query)
            # relations_data = extract_course_relations(current_query)
            # reverse_data   = extract_course_relations_reverse(current_query)
            # period_data    = extract_course_period(current_query)
            # prereq_data    = extract_course_prereq(current_query)    

            current_id       = get_course_id_8(general_data)
            current_syllabus = get_syllabus(general_data)
            result_dict[current_id] = current_syllabus

            time.sleep(random.uniform(0.5, 1.5))
    finally:
        with open('res.json', 'w') as out:
            json.dump(result_dict, out)
        

if __name__ == '__main__':
    main()




