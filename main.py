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
    output_path = 'res.json'


    year = '2025'
    season = period.Period.WINTER

    with open(path_to_raw_input) as f:
        raw_input = json.load(f)

    try:
        with open(output_path) as f:
            result_dict = json.load(f)
        print(f"Resuming - {len(result_dict)} already done")
    except FileNotFoundError:
        result_dict = {}

    already_done = result_dict.keys()
    current_query = CourseQuery('12345678', year, season)

    result_dict = {}

    try:
        for i,id in enumerate(raw_input['ids']):
            current_query.set_course_id(id)
            if current_query.course_id in already_done:
                print(i, id, '- skip')
                continue


            current_id       = get_course_id_8(general_data)
            current_syllabus = get_syllabus(general_data)
            result_dict[current_id] = current_syllabus

            time.sleep(random.uniform(0.5, 1.5))
    finally:
        with open('res.json', 'w') as out:
            json.dump(result_dict, out)
        

if __name__ == '__main__':
    main()




