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

    try:
        for i,id in enumerate(raw_input['ids']):
            current_query.set_course_id(id)
            if current_query.course_id in already_done:
                print(i, id, '- skip')
                continue

            print(i, id)

            try:
                general_data     = extract_course_general(current_query)
                # relations_data = extract_course_relations(current_query)
                # reverse_data   = extract_course_relations_reverse(current_query)
                # period_data    = extract_course_period(current_query)
                # prereq_data    = extract_course_prereq(current_query)    

                current_id       = get_course_id_8(general_data)
                current_syllabus = get_syllabus(general_data)

                syllabus_snippet = current_syllabus[:80] if current_syllabus else "(empty syllabus)"
                print(f"  ID: {current_id} | syllabus: {syllabus_snippet}")

                result_dict[current_id] = current_syllabus
            except Exception as e:
                print(f"something went wrong with {current_query}, skipping - {e}")
                continue

            if i > 0 and i % 20 == 0:
                pause = random.uniform(30, 60)
                print(f"|-)> Taking a break for {pause}s...")
                save(result_dict, output_path)
            else:
                pause = random.uniform(3, 7)


            time.sleep(pause)
    finally:
        save(result_dict, output_path)
        

if __name__ == '__main__':
    main()




